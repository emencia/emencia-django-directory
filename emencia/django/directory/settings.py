"""Settings for emencia.django.directory"""
from django.conf import settings
from django.utils.translation import gettext_lazy as _

MEDIA_URL = getattr(settings, 'DIRECTORY_MEDIA_URL', '/edd/')

USE_WORKGROUPS = getattr(settings, 'DIRECTORY_USE_WORKGROUPS', False)

PAGINATION = getattr(settings, 'DIRECTORY_PAGINATION', 20)

EDN_INSTALLED = 'emencia.django.newsletter' in getattr(settings, 'INSTALLED_APPS', [])
SORL_THUMBNAIL_INSTALLED = 'sorl.thumbnail' in getattr(settings, 'INSTALLED_APPS', [])

CUSTOM_CIVILITIES = []
for code, civility in getattr(settings, 'DIRECTORY_CUSTOM_CIVILITIES', ()):
    CUSTOM_CIVILITIES.append((code, _(civility)))
CUSTOM_CIVILITIES = tuple(CUSTOM_CIVILITIES)
