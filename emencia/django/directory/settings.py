"""Settings for emencia.django.directory"""
from django.conf import settings

EDN_INSTALLED = 'emencia.django.newsletter' in getattr(settings, 'INSTALLED_APPS', [])


