from common import *
from accounts import *
from secrets import SENTRY_DSN


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

PAYPAL_SETTINGS = {
    'url': 'https://www.sandbox.paypal.com/cgi-bin/webscr',
    'button_ids': {
        'Individual': None,
        'Standard Business': "AAAAAAAAAAAAA",
        'Premier Business': "AAAAAAAAAAAAA",
        'Nonprofit': "AAAAAAAAAAAAA",
        'Freelancer': "AAAAAAAAAAAAA",
    }
}

RAVEN_CONFIG = {
    'dsn': None
}

try:
    from ignore import *
except ImportError:
    print "No settings.ignore found.  You can create one to locally override settings."
