from django.test import TestCase
from accounts.models import Email


class SignupTests(TestCase):

    def test_first_stage_give_email(self):
        address = 'dingo@dingo.com'
        self.assertFalse(Email.objects.filter(address=address).exists())

        self.client.post('/accounts/signup/', {'address': 'dingo@dingo.com'})
        self.assertTrue(Email.objects.filter(address=address).exists())