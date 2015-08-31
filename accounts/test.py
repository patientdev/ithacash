from django.test import TestCase
from django.test.client import RequestFactory
from hendrix.utils.test_utils import AsyncTestMixin
from accounts.models import Email, IthacashAccount
from mock import patch
import mandrill
from accounts.views import review


class SignupPhaseOneTests(AsyncTestMixin, TestCase):

    def test_first_stage_give_email(self):
        address = 'dingo@dingo.com'
        self.assertFalse(Email.objects.filter(address=address).exists())

        self.client.post('/accounts/signup/', {'address': address})
        self.assertTrue(Email.objects.filter(address=address).exists())

        test_user_object = Email.objects.get(address=address)
        most_recent_confirmation_key = test_user_object.most_recent_confirmation_key
        self.assertTrue(Email.objects.filter(most_recent_confirmation_key=most_recent_confirmation_key).exists())

        session = self.client.session
        self.client.post('/accounts/await-confirmation/', {session['most_recent_confirmation_key']: most_recent_confirmation_key})

        # Now let's look at the email that's sent.
        self.assertNumCrosstownTasks(1)
        email_sender = self.next_task()

        # We mock mandrill so as not to send a real email every time we run the test.
        with patch.object(mandrill.Messages, 'send') as mock_email_sender:
            email_sender()
            self.assertEqual(mock_email_sender.call_count, 1)

            email_sent_to = mock_email_sender.call_args[0][0]['to'][0]['email']
            self.assertEqual(email_sent_to, address)

    def test_confirm_email(self):
        email_object = Email.objects.create(address="test@test.com")
        key = email_object.most_recent_confirmation_key

        self.assertIsNotNone(key)
        self.assertIsNone(email_object.confirmed)

        email_object.confirm(key)
        self.assertIsNotNone(email_object.confirmed)

    def test_confirm_email_view(self):
        email_object = Email.objects.create(address="test@test.com")
        key = email_object.most_recent_confirmation_key
        response = self.client.get('/accounts/create_account/%s' % key)

        self.assertEqual(response.status_code, 200)

        same_email_object = Email.objects.get(most_recent_confirmation_key=email_object.most_recent_confirmation_key)
        self.assertEqual(email_object, same_email_object)
        self.assertTrue(same_email_object.confirmed)


class CreateAccountTests(TestCase):

    account_post_data = {
        u'username': u'joe_individual',
        u'city': u'Ithaca',
        u'account_type': u'Individual',
        u'address_2': u'',
        u'entity_name': u'n/a',
        u'state': u'NY',
        u'electronic_signature': u'asdas',
        u'tin': u'445556154',
        u'is_ssn': u'True',
        u'phone_mobile': u'',
        u'address_1': u'4 llama road',
        u'full_name': u'Some Guy I guess',
        u'phone_landline': u'+16075554141',
        u'zip_code': u'14850'
    }

    def test_create_account_with_invalid_data(self):
        email = Email.objects.create(address="nobody@nothing.com")

        r = RequestFactory()
        r.method = "POST"
        r.POST = {'most_recent_confirmation_key': email.most_recent_confirmation_key}
        r.META = {}

        response = review(r)
        self.assertIsNotNone(response)

    def test_create_account_with_valid_data(self):
        email = Email.objects.create(address="nobody@nothing.com")
        self.account_post_data['most_recent_confirmation_key'] = email.most_recent_confirmation_key

        r = RequestFactory()
        r.method = "POST"
        r.POST = self.account_post_data
        r.META = {}

        response = review(r)
        self.assertEqual(response.status_code, 200)
        return response

    def test_create_account_with_valid_data_results_in_account_objects(self):
        self.assertFalse(IthacashAccount.objects.exists())

        response = self.test_create_account_with_valid_data()

        self.assertTrue(IthacashAccount.objects.exists())
