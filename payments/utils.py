import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class PaypalValidator(object):

    def validate_paypal_ipn(self, params_dict):
        params_dict['cmd']='_notify-validate'
        response = requests.post(settings.PAYPAL_SETTINGS['url'], data=params_dict)

        valid = False  # Until proven otherwise.

        if response.content == "INVALID":
            logger.info('Invalid Paypal request.  Might be strange folk abroad.  Params were: %s' % params_dict)
        elif response.content == "VERIFIED":
            logger.info('Validated Paypal payament with params: %s' % params_dict)
            valid = True
        else:
            logger.warning("Paypal did not give a properly formatted response to params: %s" % params_dict)
        return valid