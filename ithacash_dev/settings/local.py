from common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


try:
    from ignore import *
except ImportError:
    print "No settings.ignore found.  You can create one to locally override settings."
