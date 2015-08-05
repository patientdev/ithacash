from common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

PAYPAL_SETTINGS = {
    'url': 'https://www.sandbox.paypal.com/cgi-bin/webscr',
    'button_ids': {
        'StandardBusiness': "KT959QR33959U",
    }
}

try:
    from ignore import *
except ImportError:
    print "No settings.ignore found.  You can create one to locally override settings."
