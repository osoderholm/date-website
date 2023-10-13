import os

from .base_settings import *


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
] + INSTALLED_APPS_BASE

# Set the name to the "root" app of the site
PROJECT_NAME = 'date'
PROJECT_TMPL = os.path.join(BASE_DIR, PROJECT_NAME, '/templates/')

ROOT_URLCONF = PROJECT_NAME + '.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['core/templates', PROJECT_TMPL],
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
            ],
        },
    },
]

STATICFILES_DIRS = [os.path.join(BASE_DIR, PROJECT_NAME, 'templates/static')]
