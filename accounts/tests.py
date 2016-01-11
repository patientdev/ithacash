from django.test import TestCase
from django.test.client import RequestFactory
from hendrix.utils.test_utils import AsyncTestMixin
from accounts.models import Email, IthacashAccount
from mock import patch
import requests
import mandrill
from accounts.views import signup_step_1_confirm_email, signup_step_3_select_account_type, review
from accounts.factories import IthacashUserFactory, EmailFactory, IthacashAccountFactory
from accounts.api import register_account

from accounts.management.commands import create_and_email_csv
from base64 import b64encode


class SignupPhaseOneTests(AsyncTestMixin, TestCase):

    def test_first_stage_give_email(self):
        print 'test_first_stage_give_email'
        address = 'dingo@dingo.com'
        self.assertFalse(Email.objects.filter(address=address).exists())

    def test_confirm_email(self):
        print 'test_confirm_email'

        address = 'test@test.com'

        self.client.post('/accounts/await-confirmation/', {'address': address})
        self.assertTrue(Email.objects.filter(address=address).exists())

        email_object = Email.objects.get(address=address)
        key = email_object.most_recent_confirmation_key

        self.assertIsNotNone(key)
        self.assertIsNone(email_object.confirmed)

        # Now let's look at the email that's sent.
        self.assertNumCrosstownTasks(1)
        email_sender = self.next_task()

        # We mock mandrill so as not to send a real email every time we run the test.
        with patch.object(mandrill.Messages, 'send') as mock_email_sender:
            email_sender()
            self.assertEqual(mock_email_sender.call_count, 1)

            email_sent_to = mock_email_sender.call_args[0][0]['to'][0]['email']
            self.assertEqual(email_sent_to, address)

        email_object.confirm(key)
        self.assertIsNotNone(email_object.confirmed)

    def test_confirm_email_view(self):
        print 'test_confirm_email_view'
        email_object = Email.objects.create(address="test@test.com")
        key = email_object.most_recent_confirmation_key
        response = self.client.get('/accounts/create_account/%s' % key)

        self.assertEqual(response.status_code, 200)

        same_email_object = Email.objects.get(most_recent_confirmation_key=email_object.most_recent_confirmation_key)
        self.assertEqual(email_object, same_email_object)
        self.assertTrue(same_email_object.confirmed)


class CreateAccountTests(TestCase):

    account_post_data = {
        u'username': u'josephshmo',
        u'city': u'Ithaca',
        u'account_type': u'Individual',
        u'address_2': u'',
        u'entity_name': u'',
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
        print 'test_create_account_with_invalid_data'

        email = Email.objects.create(address="nobody@nothing.com")

        r = RequestFactory()
        r.method = "POST"
        r.POST = {'most_recent_confirmation_key': email.most_recent_confirmation_key}
        r.META = {}

        response = signup_step_1_confirm_email(r)
        self.assertIsNotNone(response)

    def test_create_account_with_valid_data(self):
        print 'test_create_account_with_valid_data'

        email = Email.objects.create(address="nobody@nothing.com")

        r = RequestFactory().get('/accounts/create_account/%s' % email.most_recent_confirmation_key)

        response = signup_step_3_select_account_type(r, email.most_recent_confirmation_key)

        self.assertEqual(response.status_code, 200)


    def test_create_account_with_valid_data_results_in_account_objects(self):
        print 'test_create_account_with_valid_data_results_in_account_objects'

        self.assertFalse(IthacashAccount.objects.exists())

        user = IthacashUserFactory()
        email = EmailFactory(owner=user)

        self.account_post_data['user_id'] = user.id

        r = RequestFactory()
        r.method = "POST"
        r.POST = self.account_post_data
        r.META = {}

        response = review(r)

        self.assertTrue(IthacashAccount.objects.exists())

        return IthacashAccount.objects.get(owner_id=user.id)

    def test_csv_export_and_email(self):
        print 'test_csv_export_and_email'

        """
        Assert that the base64 encoding of the csv_output has reached mandrill
        """

        # Give us a premade user, email, and account
        user = IthacashUserFactory()
        email = EmailFactory(owner=user)
        account = IthacashAccountFactory(owner=user)

        with patch.object(mandrill.Messages, 'send') as mock_email_sender:

            csv_processor = create_and_email_csv.Command()

            most_recent_fake_signups = csv_processor.get_most_recent_signups()

            csv_processor.map_cyclos_keys_to_ithacash_user_values(most_recent_fake_signups)
            csv_output = csv_processor.output_csv().getvalue()
            csv_processor.email_csv()

            csv_attachment = mock_email_sender.call_args[0][0]['attachments'][0]['content']
            self.assertEqual(b64encode(csv_output), csv_attachment)


class APITests(TestCase):
    def test_api_register_account(self):

        account = IthacashAccountFactory()

        r = RequestFactory()
        r.GET = {'id': account.id}
        r.META = {}

        with patch.object(IthacashAccount, 'send_awaiting_verification_message', return_value=None) as mock_email_sender:
            response = register_account(r)

            self.assertEqual(mock_email_sender.call_count, 1)
