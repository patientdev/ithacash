from common import *
from accounts import *
from secrets import SENTRY_DSN


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
    'dsn': None
}

try:
    from ignore import *
except ImportError:
    print "No settings.ignore found.  You can create one to locally override settings."
