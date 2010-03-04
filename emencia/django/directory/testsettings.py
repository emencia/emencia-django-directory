import os

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/directory.db'
INSTALLED_APPS = ['django.contrib.auth',
                  'django.contrib.contenttypes',
                  'tagging',
                  'sorl.thumbnail',
                  'emencia.django.countries',
                  'emencia.django.directory',]

LANGUAGE_CODE = 'fr'

LANGUAGES = (
    ('fr', 'French'),
    ('en', 'English'),
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    )

