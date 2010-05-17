"""Settings for emencia.django.directory"""
from django.conf import settings

MEDIA_URL = getattr(settings, 'DIRECTORY_MEDIA_URL', '/edd/')

USE_WORKGROUPS = getattr(settings, 'DIRECTORY_USE_WORKGROUPS', False)

EDN_INSTALLED = 'emencia.django.newsletter' in getattr(settings, 'INSTALLED_APPS', [])
SORL_THUMBNAIL_INSTALLED = 'sorl.thumbnail' in getattr(settings, 'INSTALLED_APPS', [])

CUSTOM_CIVILITIES = getattr(settings, 'DIRECTORY_CUSTOM_CIVILITIES', ())
