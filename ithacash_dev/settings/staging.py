from common import *
from accounts import *
from secrets import PRODUCTION_DATABASE_PASSWORD

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
    'url': 'https://www.paypal.com/cgi-bin/webscr',
    'button_ids': {
        'Individual': None,
        'Standard Business': "NVJ455UBSLFH8",
        'Premier Business': "4M72KKRAMTXPL",
        'Nonprofit': "SKU9BAQ3ZJUVU",
        'Freelancer': "77D4TSU2PGL92",
    }
}

RAVEN_CONFIG = {
    'dsn': SENTRY_DSN,
}
