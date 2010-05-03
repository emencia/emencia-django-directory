"""Command for importing profile into emencia.django.directory"""
from django.template.defaultfilters import slugify
from django.core.management.base import LabelCommand

from emencia.django.directory.models import Nature
from emencia.django.countries.models import Country
from emencia.django.directory.models import Profile
from emencia.django.directory.models import Category
from emencia.django.directory.models import Section
from emencia.django.directory.models import Company

from utils import *

COLUMNS = ['civility', 'last_name', 'first_name',
           'username', 'password', 'is_active', 'visible',
           'email', 'phone', 'mobile', 'fax',
           'address_1', 'address_2', 'address_comments',
           'postal_code', 'city', 'country',
           'lat', 'lng', 'reference', 'function',
           'companies', 'language', 'birthdate',
           'nature', 'categories', 'sections', 'tags',
           'comments']

class Command(LabelCommand):
    """Command of injection"""
    args = 'directory.csv'
    label = 'file.csv'
    help = 'Import profiles to emencia.django.directory from a csv file'

    def handle_label(self, filename, **options):
        verbosity = int(options['verbosity'])
        print '* Launching import of directory'

        init_dbengine()
        PROFILE_CACHE = init_cache()
        data_lines = init_data(filename)

        for line in data_lines:
            attr = self.format(extract_values(line, COLUMNS))
            if attr['username'] not in PROFILE_CACHE:
                profile_attr = self.clean_profile(attr)
                profile = Profile(**profile_attr)
                profile.save()
                profile.sections.add(*attr['sections'])
                profile.categories.add(*attr['categories'])
                profile.companies.add(*attr['companies'])

                if verbosity:
                    print '- %s created' % profile.__unicode__()
                PROFILE_CACHE.add(attr['username'])

    def clean_profile(self, data):
        cleaned_data = data.copy()
        del cleaned_data['sections']
        del cleaned_data['companies']
        del cleaned_data['categories']
        return cleaned_data

    def format(self, data):
        data['civility'] = convert_civility(data['civility'].lower())

        if not data['first_name']:
            data['first_name'] = ''
            
        if not data['last_name']:
            data['last_name'] = ''

        if not data['username']:
            data['username'] = get_username(data)

        data['visible'] = convert_bool(data['visible'])
        data['is_active'] = convert_bool(data['is_active'])

        data['companies'] = convert_abstract(data['companies'], Company)
        data['sections'] = convert_abstract(data['sections'], Section)
        data['categories'] = convert_abstract(data['categories'], Category)
        data['nature'] = convert_abstract(data['nature'], Nature)[0]
        data['country'] = convert_country(data['country'])

        data['birthdate'] = None
        data['language'] = data['language'].lower()#'fr'

        return data








