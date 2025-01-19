"""
Django settings for date project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
# update

import os
import sys
import json

import environ

from .dependencies.ckeditor import *  # noqa


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    DEVELOP=(bool, False),
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-date development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', str, 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', bool, False)

DEVELOP = env('DEVELOP', bool, False)

# This gets set only when tests are ran with date-test command
TEST = env('TEST', bool, False)

ALLOWED_HOSTS = json.loads(env('ALLOWED_HOSTS', str, '[]'))

CSRF_TRUSTED_ORIGINS = json.loads(env('ALLOWED_ORIGINS', str, '[]'))


if not DEVELOP:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True


def get_installed_apps(proj_apps):
    return [
        'daphne',
        'date',
        'members',
        *proj_apps,
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'admin_ordering',
        'django_ckeditor_5',
        'channels',
        'storages',
        'django_tables2',
        'django_filters',
        'bootstrap3',
        'django_cleanup',  # Should be places last
    ]


# Common template config
COMMON_TEMPLATE_DIRS = [
    'templates/common',
    'templates/common/members',
]


COMMON_CONTEXT_PROCESSORS = [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.template.context_processors.i18n',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'staticpages.context_processors.get_categories',
    'staticpages.context_processors.get_urls',
    'core.context_processors.captcha_context',
    'core.context_processors.apply_content_variables',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'date.middleware.LangMiddleware',
    'date.middleware.HTCPCPMiddleware',
]


WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.routing.application'


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_DATABASE', str, 'postgres'),
        'USER': env('DB_USERNAME', str, 'postgres'),
        'PASSWORD': env('DB_PASSWORD', default=''),
        'HOST': env('DB_HOST', str, 'db'),
        'PORT': env('DB_PORT', int, 5432)
    }
}

# Skip pgbouncer for running tests
if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default']['HOST'] = 'db'
    DATABASES['default']['NAME'] = 'test_db'

CONN_MAX_AGE = 600

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": env("REDIS_SERVER", str, "redis://redis:6379"),
    },
}

# Custom members model
AUTH_USER_MODEL = 'members.Member'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'members.backends.AuthBackend',
)


def get_staff_groups(default_groups: list):
    """Add extra staff groups from environment variable to default_groups."""
    default_groups.extend(json.loads(os.environ.get('EXTRA_STAFF_GROUPS', '[]')))
    return default_groups

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/


LOCALE_PATHS = (
    'locale',
)

LANG_FINNISH = 'fi'
LANG_SWEDISH = 'sv'

LANGUAGE_CODE = LANG_SWEDISH

TIME_ZONE = 'Europe/Helsinki'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DECIMAL_INPUT_FORMATS = ()

DATE_INPUT_FORMATS = ('%d.%m.%Y', '%Y-%m-%d')

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

PROJECT_NAME = os.environ.get("PROJECT_NAME", "date")
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cloudflare captcha config
TURNSTILE_SECRET_KEY = env("CF_TURNSTILE_SECRET_KEY", str, "")
CAPTCHA_SITE_KEY = env("CF_TURNSTILE_SITE_KEY", str, "")

# S3 conf using django storages
USE_S3 = env('USE_S3', bool, False)

STORAGES = {
    "default": {
        "BACKEND": 'django.core.files.storage.FileSystemStorage',
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    }
}

if USE_S3:
    # aws settings
    AWS_S3_ENDPOINT_URL = env('AWS_S3_ENDPOINT_URL')
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_QUERYSTRING_AUTH = True
    AWS_QUERYSTRING_EXPIRE = 3600

    # s3 public media settings
    PRIVATE_MEDIA_LOCATION = env('PRIVATE_MEDIA_LOCATION')
    PUBLIC_MEDIA_LOCATION = env('PUBLIC_MEDIA_LOCATION')
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{PRIVATE_MEDIA_LOCATION}/'

    STORAGES["default"] = {  # TODO allow setting this to local
        "BACKEND": "core.storage_backends.PrivateMediaStorage",
        "OPTIONS": {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "custom_domain": False,
            "querystring_auth": AWS_QUERYSTRING_AUTH,
            "querystring_expire": AWS_QUERYSTRING_EXPIRE,
            "location": PRIVATE_MEDIA_LOCATION,
        }
    }
    STORAGES["public_media"] = {
        "BACKEND": "core.storage_backends.PublicMediaStorage",
        "OPTIONS": {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "custom_domain": False,
            "location": PUBLIC_MEDIA_LOCATION,
        }
    }

else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

    # Not in use when not using s3 but need to be set in order not to cause errors
    PRIVATE_MEDIA_LOCATION = 'media/private'
    PUBLIC_MEDIA_LOCATION = 'media/public'
    AWS_STORAGE_BUCKET_NAME = "media"

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'

LOGIN_URL = '/members/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = env('EMAIL_HOST', str, '')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', str, '')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', str, '')
EMAIL_PORT = 587

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', str, '')
EMAIL_HOST_RECEIVER = env('EMAIL_HOST_RECEIVER', str, '')

# Celery Configuration
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 3000

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django_auth_ldap': {
            'handlers': ['console_debug'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'date': {
            'handlers': ['console_debug'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'daphne': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

EXPERIMENTAL_FEATURES = []
