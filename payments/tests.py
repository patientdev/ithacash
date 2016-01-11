from django.test import TestCase
from django.test.client import RequestFactory
from mock.mock import patch
from accounts.factories import IthacashAccountFactory
from accounts.models import IthacashAccount, IthacashUser
import payments
from payments.models import SignUpPayment
from payments.views import paypal_ipn_endpoint
from payments.utils import PaypalValidator

SAMPLE_PAYPAL_IPN_PAYLOAD = {
    u'protection_eligibility': u'Eligible',
    u'last_name': u'Buyer',
    u'txn_id': u'2FL55751505704848',
    u'shipping_method': u'Default',
    u'shipping_discount': u'0.00',
    u'receiver_email': u'button-guy@ithacash.org', u'payment_status': u'Completed', u'payment_gross': u'1.00', u'tax': u'0.00', u'residence_country': u'US', u'cmd': u'notify-validate', u'address_state': u'CA', u'payer_status': u'verified', u'txn_type': u'web_accept', u'address_street': u'1 Main St', u'handling_amount': u'0.00', u'payment_date': u'14:27:04 Aug 05, 2015 PDT', u'custom': u'account_1', u'first_name': u'New', u'btn_id': u'3192831', u'item_name': u'(Test) Standard Business', u'address_country': u'United States', u'charset': u'windows-1252', u'notify_version': u'3.8', u'address_name': u'New Buyer', u'test_ipn': u'1', u'item_number': u'', u'receiver_id': u'XVXXCB8749N22', u'transaction_subject': u'account_1', u'business': u'button-guy@ithacash.org', u'payerid': u'2VRDXFJNECEUJ', u'discount': u'0.00', u'verify_sign': u'A-X.bgkHiBJDUeODT9kVdmzwhS1aAbhjO5OJZEUPE1ntThQFudFDZSiD', u'address_zip': u'95131', u'payment_fee': u'0.33', u'address_country_code': u'US', u'address_city': u'San Jose', u'address_status': u'confirmed', u'insurance_amount': u'0.00', u'mc_fee': u'0.33', u'mc_currency': u'USD', u'shipping': u'0.00', u'payer_email': u'new-buyer@ithacash.org', u'payment_type': u'instant', u'mc_gross': u'1.00', u'ipn_track_id': u'8f1adeb7339d', u'quantity': u'1'}


class PaypalTests(TestCase):

    def test_ipn_endpoint_new_account(self):
        print 'test_ipn_endpoint_new_account'

        r = RequestFactory()
        r.method = "POST"
        r.POST = SAMPLE_PAYPAL_IPN_PAYLOAD
        r.META = {}

        self.assertFalse(SignUpPayment.objects.exists())

        # TODO: Use bamboo_boy.
        account = IthacashAccountFactory()

        payment_amount = 80.00
        r.POST['custom'] = "account_%s" % account.id
        r.POST['payment_gross'] = payment_amount
        r.POST['payment_status'] = 'Completed'

        with patch.object(PaypalValidator, 'validate_paypal_ipn', return_value=True) as mock_paypal_ipn:
            with patch.object(IthacashAccount, 'send_awaiting_verification_message', return_value=None) as mock_email_sender:
                response = paypal_ipn_endpoint(r)
                self.assertEqual(account.payments.count(), 1)

                payment = account.payments.all()[0]
                self.assertEqual(payment.signuppayment.amount, payment_amount)

                self.assertEqual(mock_paypal_ipn.call_count, 1)

    def test_ipn_endpoint_direct_transation(self):
        print 'test_ipn_endpoint_direct_transation'

        '''For PayPal transactions initiated directly through PayPal rather than at the end of our signup form'''

        r = RequestFactory()
        r.method = "POST"
        r.POST = SAMPLE_PAYPAL_IPN_PAYLOAD
        r.META = {}

        # Direct transactions won't recieve and therefore won't send a 'custom' POST key, so remove it from our sample payload
        r.POST.pop('custom')

        with patch.object(PaypalValidator, 'validate_paypal_ipn', return_value=True) as mock_paypal_ipn:
            response = paypal_ipn_endpoint(r)
            self.assertEqual('PROCESSED.', response.content)
