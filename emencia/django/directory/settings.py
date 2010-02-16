"""Settings for emencia.django.directory"""
from django.conf import settings

EDN_REGISTERED = 'emencia.django.newsletter' in getattr(settings, 'INSTALLED_APPS', [])


