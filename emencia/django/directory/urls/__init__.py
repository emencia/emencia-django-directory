"""Urls for the emencia.django.directory"""
from django.conf.urls.defaults import *



urlpatterns = patterns('',
                       url(r'^profiles/', include('emencia.django.directory.urls.profile')),
                       url(r'^companies/', include('emencia.django.directory.urls.company')),
                       )

