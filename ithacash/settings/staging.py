from common import *
from accounts import *
from secrets import PRODUCTION_DATABASE_PASSWORD, SENTRY_DSN

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'ithacash.com', '45.55.80.254']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ithacash",
        "USER": "ithacash_db_user",
        "PASSWORD": PRODUCTION_DATABASE_PASSWORD,
        "HOST": "localhost",
        "PORT": "5432",
    }
}

PAYPAL_SETTINGS = {
    'url': 'https://www.sandbox.paypal.com/cgi-bin/webscr',
    'button_ids': {
        'Individual': None,
        'Standard Business': "KT959QR33959U",
        'Premier Business': "4M72KKRAMTXPL",
        'Nonprofit': "SKU9BAQ3ZJUVU",
        'Freelancer': "77D4TSU2PGL92",
    }
}

RAVEN_CONFIG['name'] = "Staging"
RAVEN_CONFIG['site'] = 'staging.ithacash.com'
