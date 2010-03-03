"""Context Processors for emencia.django.directory"""
from emencia.django.directory.settings import MEDIA_URL

def media(request):
    """Adds media-related context variables to the context"""
    return {'DIRECTORY_MEDIA_URL': MEDIA_URL}
