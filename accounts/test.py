from django.test import TestCase
from hendrix.utils.test_utils import AsyncTestMixin
from accounts.models import Email
from mock import patch
import mandrill


class SignupTests(AsyncTestMixin, TestCase):

    def test_first_stage_give_email(self):
        address = 'dingo@dingo.com'
        self.assertFalse(Email.objects.filter(address=address).exists())

        test_recipient = 'dingo@dingo.com'
        self.client.post('/accounts/signup/', {'address': test_recipient})
        self.assertTrue(Email.objects.filter(address=address).exists())

        # Now let's look at the email that's sent.
        self.assertNumCrosstownTasks(1)
        email_sender = self.next_task()

        with patch.object(mandrill.Messages, 'send') as mock_email_sender:
            email_sender()
            self.assertEqual(mock_email_sender.call_count, 1)

            email_sent_to = mock_email_sender.call_args[0][0]['to'][0]['email']
            self.assertEqual(email_sent_to, test_recipient)

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
