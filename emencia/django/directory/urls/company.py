"""Urls for the emencia.django.directory Company"""
from django.conf.urls.defaults import *

from emencia.django.directory.models import Company
from emencia.django.directory.settings import PAGINATION

company_conf = {'queryset': Company.objects.published(),
                'paginate_by': PAGINATION,}

company_conf_detail = company_conf.copy()
del company_conf_detail['paginate_by']

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           company_conf, 'directory_company_list'),
                       url(r'^(?P<slug>[-\w]+)$', 'object_detail',
                           company_conf_detail, 'directory_company_detail'),
                       )

