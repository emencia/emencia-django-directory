"""Settings for emencia.django.directory"""
from django.conf import settings

MEDIA_URL = getattr(settings, 'DIRECTORY_MEDIA_URL', '/edd/')

EDN_INSTALLED = 'emencia.django.newsletter' in getattr(settings, 'INSTALLED_APPS', [])


