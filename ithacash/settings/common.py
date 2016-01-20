"""
Django settings for ithacash project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https:/docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https:/docs.djangoproject.com/en/1.8/ref/settings/
"""
from secrets import SECRET_KEY, MANDRILL_API_KEY, MAILCHIMP_API_KEY, SENTRY_DSN

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https:/docs.djangoproject.com/en/1.8/howto/deployment/checklist/
# Application definition

SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'accounts',
    'payments',
    'pages',
    'raven.contrib.django.raven_compat',
    'django.contrib.sitemaps',
    'staff',
)

MIDDLEWARE_CLASSES = (
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

AUTHENTICATION_BACKENDS = [
    'staff.auth.IthacashStaffBackend',
    'django.contrib.auth.backends.ModelBackend'
]

ROOT_URLCONF = 'ithacash.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\','/')],
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'ithacash.wsgi.application'

# Internationalization
# https:/docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https:/docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'ithacash/static'
STATICFILES_DIRS = (BASE_DIR, 'ithacash/static')
STATIFILES_FINDERS = ["django.contrib.staticfiles.finders.FileSystemFinder",
 "django.contrib.staticfiles.finders.AppDirectoriesFinder"]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'pages/media'

HENDRIX_CHILD_RESOURCES = (
    'hendrix.contrib.resources.static.DefaultDjangoStaticResource',
    # uncomment if you would like to serve the django admin static files
    # 'hendrix.contrib.resources.static.DjangoAdminStaticResource',
)

RAVEN_CONFIG = {
    'dsn': SENTRY_DSN
    # Need proper versioning for this
    # 'release': raven.fetch_git_sha(os.path.dirname(__file__))
}

# django-encrypted-fields
ENCRYPTED_FIELDS_KEYDIR = os.path.join(BASE_DIR, 'ithacash/settings/secrets/fieldkeys')

AUTH_USER_MODEL = 'accounts.IthacashUser'

# django-phonenumberfield
PHONENUMBER_DEFAULT_REGION = 'US'
PHONENUMBER_DB_FORMAT = 'NATIONAL'