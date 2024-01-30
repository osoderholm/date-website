import os

from .base_settings import * #NOQA

# export DJANGO_SETTINGS_MODULE=MyDjangoApp.settings

# Apps to include for the site 
INSTALLED_APPS = [
    'date',
    'staticpages',
    'news',
    'events',
    'members',
    'ads',
    'event_calendar',
    'social',
    'polls',
    'ctf',
    'daphne',
    'archive.apps.ArchiveConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_ordering',
    'ckeditor',
    'channels',
    'storages',
    'django_tables2',
    'django_filters',
    'bootstrap3',
    'django_cleanup',
]

# Set the name to the "root" app of the site
# PROJECT_NAME = env('project_name')
PROJECT_NAME = 'date'
PROJECT_TMPL = PROJECT_NAME + '/templates/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, PROJECT_NAME, '/templates/static')
STATIC_URL = '/static/'

ROOT_URLCONF = PROJECT_NAME + '.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_TMPL],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'staticpages.context_processors.get_pages',
                'staticpages.context_processors.get_categories',
                'staticpages.context_processors.get_urls',
                PROJECT_NAME + '.template_variables.template_variables'
            ],
        },
    },
]

STATICFILES_DIRS = [os.path.join(BASE_DIR, PROJECT_NAME, 'templates/static')]
