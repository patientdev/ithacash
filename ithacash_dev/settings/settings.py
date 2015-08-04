from common import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "kayemyles_db",
        "USER": "kayemyles",
        "PASSWORD": DATABASE_PASSWORD,
        "HOST": "localhost",
        "PORT": "5432",
    }
}
