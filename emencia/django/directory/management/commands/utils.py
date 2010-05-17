"""Utils for import_edd"""
import sys
from datetime import datetime, timedelta

from django.conf import settings
from django.db import connection
from django.contrib.auth.models import Group
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_unicode

from emencia.django.countries.models import Country
from emencia.django.directory.models import Profile
from emencia.django.directory.models import WorkGroup
from emencia.django.directory.admin.abstractcategory import WORKGROUP_RELATIONS

def init_dbengine():
    """Prepare the dbengine"""
    if settings.DATABASE_ENGINE == 'sqlite3':
        print '-- Sqlite 3 engine detected, unlocking FS protections.'
        cursor = connection.cursor()
        cursor.execute('PRAGMA temp_store = MEMORY;')
        cursor.execute('PRAGMA synchronous = OFF;')

def init_cache():
    """Cache profile inserted"""
    cache = set(Profile.objects.values_list('username', flat=True))
    print '-- Cache ready, %i profiles found.' % len(cache)
    return cache

def init_data(filename):
    """Return the data in lines"""
    source = open(filename, 'r')
    lines = source.readlines()
    source.close()

    if lines[0].startswith('"Civilit'):
        del lines[0]

    print '-- %i profiles found in source file' % len(lines)
    return lines

def bind_values(values, columns=[]):
    """Bind values to a dict"""
    data = {}
    for i in range(min([len(values), len(columns)])):
        data[columns[i]] = values[i]
    return data

def extract_values(line, columns):
    """Return values as a dict from a line"""
    return bind_values([v.strip('"').strip()
                        for v in smart_unicode(line).split(';')],
                       columns)

def convert_bool(value, valid='oui'):
    """Convert custom string value to a bool"""
    if value:
        if value.lower().strip() == valid.lower():
            return True
    return False

def convert_country(value):
    """Convert string to a Country object"""
    try:
        return Country.objects.get(iso=value[:2])
    except:
        return Country.objects.get_or_create(iso='UN', defaults={
            'name': 'UNKNOW',
            'printable_name': 'Unknow'})[0]

def convert_abstract(value, model, workgroups):
    """Convert string to a abstracted model"""
    if not value:
        return [model.objects.get_or_create(name='N/C', slug='n-c')[0]]
    abstracts = [model.objects.get_or_create(name=abstract,
                                             slug=slugify(abstract))[0]
                 for abstract in value.split(',')]

    relation = WORKGROUP_RELATIONS[model]
    for workgroup in workgroups:        
        getattr(workgroup, relation).add(*abstracts)
    return abstracts

CIVILITY_REVERSE = {'unknown': 0, 'inconnu': 0,
                    'mlle': 1, 'mle': 1, 'melle': 1,
                    'ms': 1, 'miss': 1,
                    'mme': 2, 'madame': 2, 'lady': 2,
                    'mr': 3, 'm.': 3, 'm': 3,
                    'monsieur': 3, 'mmr': 3,
                    'mlle, mr': 4, 'mle,mr': 4,
                    'mme, mr': 5, 'mr, mme': 5,
                    'mme,mr': 5, 'm/s': 5, 'mr/mrs': 5,
                    'mr & mrs': 5,
                    'mmes': 6, 'mrs': 7,
                    'ste': 8, 'docteur': 9, 'dr': 9,
                    'sheik': 10, 'lord': 11}

def convert_civility(value):
    """Convert string to civility"""
    if not value:
        return Profile.CIVILITY_CHOICES[0][0]
    else:
        return CIVILITY_REVERSE[value]

def convert_workgroups(value):
    workgroups = []
    for wg in value.split(','):
        group, created = Group.objects.get_or_create(name=wg)
        workgroup, created = WorkGroup.objects.get_or_create(name=wg,
                                                             group=group)
        workgroups.append(workgroup)
    return workgroups

def generate_username(attrs, suffix=''):
    return str(slugify(' '.join([attrs['last_name'], attrs['first_name'], 
                                 attrs['reference'], attrs['companies'], suffix])))


def get_username(attrs):
    """Generate unique username"""
    username = generate_username(attrs)
    profiles = Profile.objects.filter(username__icontains=username)
    if not profiles:
        return username
    else:
        return generate_username(attrs, str(profiles.count() + 1))

def format_name(name):
    names = name.split('-')
    return '-'.join([name.capitalize() for name in names])
    
class ProgressLine(object):
    """Object for making progress line status"""

    def __init__(self, rows):
        self.row = 0
        self.rows = rows
        self.start_time = datetime.now()

    def top(self):
        self.row += 1

        elapsed_time = datetime.now() - self.start_time        
        remaining_time = timedelta(seconds=int(float(self.rows * elapsed_time.seconds) / self.row) - elapsed_time.seconds)
        percent_done = (float(self.row) / float(self.rows)) * 100
        
        sys.stdout.write('\rScanning entry %i/%i, %s elapsed, %s remaining => %.5f%%' %
                         (self.row, self.rows,
                          str(elapsed_time).split('.')[0],
                          str(remaining_time).split('.')[0],
                          percent_done))
        sys.stdout.flush()
                      

    
