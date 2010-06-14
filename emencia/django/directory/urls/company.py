"""Urls for the emencia.django.directory Company"""
from django.conf.urls.defaults import *

from emencia.django.directory.models import Company

company_conf = {'queryset': Company.objects.published()}

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           company_conf, 'directory_company_list'),
                       url(r'^(?P<slug>[-\w]+)$', 'object_detail',
                           company_conf, 'directory_company_detail'),
                       )

