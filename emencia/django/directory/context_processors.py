"""Context Processors for emencia.django.directory"""
from emencia.django.directory.settings import MEDIA_URL
from emencia.django.directory.settings import EDN_INSTALLED

def media(request):
    """Adds media-related context variables to the context"""
    return {'DIRECTORY_MEDIA_URL': MEDIA_URL,
            'EDN_INSTALLED': EDN_INSTALLED}
