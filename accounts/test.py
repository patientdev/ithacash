from django.test import TestCase
from hendrix.utils.test_utils import AsyncTestMixin
from accounts.models import Email


class SignupTests(AsyncTestMixin, TestCase):

    def test_first_stage_give_email(self):
        address = 'dingo@dingo.com'
        self.assertFalse(Email.objects.filter(address=address).exists())

        self.client.post('/accounts/signup/', {'address': 'dingo@dingo.com'})
        self.assertTrue(Email.objects.filter(address=address).exists())

        # Now let's look at the email that's sent.
        self.assertNumCrosstownTasks(1)
        email_sender = self.next_task()

        print email_sender

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
        self.fail()