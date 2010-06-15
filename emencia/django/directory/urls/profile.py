"""Urls for the emencia.django.directory Profile"""
from django.conf.urls.defaults import *

from emencia.django.directory.models import Profile
from emencia.django.directory.settings import PAGINATION

profile_conf = {'queryset': Profile.objects.published(),
                'paginate_by': PAGINATION,}

profile_conf_detail = profile_conf.copy()
del profile_conf_detail['paginate_by']
profile_conf_detail['slug_field'] = 'username'

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           profile_conf, 'directory_profile_list'),
                       url(r'^(?P<slug>[-\w]+)$', 'object_detail',
                           profile_conf_detail, 'directory_profile_detail'),
                       )


urlpatterns += patterns('emencia.django.directory.views.profile',
                        url(r'^company/(?P<slug>[-\w]+)$',
                            'view_company_profile_list',
                            name='directory_company_profile_list'),
                        )

