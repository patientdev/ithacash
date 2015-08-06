from common import *
from secrets import PRODUCTION_DATABASE_PASSWORD

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
        'Standard Business': "2GVP4YZDG27ML",
        'Premier Business': "4M72KKRAMTXPL",
        'Nonprofit': "SKU9BAQ3ZJUVU",
        'Freelancer': "5SFX422BMEQJS",
    }
}
