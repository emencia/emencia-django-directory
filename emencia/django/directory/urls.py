"""Urls for the emencia.django.directory"""
from django.conf.urls.defaults import *

from emencia.django.directory.models import Profile

profile_conf = {'queryset': Profile.objects.published()}

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           profile_conf, 'directory_profile_list'),
                       url(r'^(?P<slug>[-\w]+)$', 'object_detail',
                           profile_conf, 'directory_profile_detail'),
                       )

