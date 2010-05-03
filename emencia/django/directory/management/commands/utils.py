"""Utils for import_edd"""
from django.conf import settings
from django.db import connection
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_unicode

from emencia.django.countries.models import Country
from emencia.django.directory.models import Profile

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
    if not value:
        return Country.objects.get(iso='FR')
    # WARNING
    #return Country.objects.get(iso=value)
    try:
        return Country.objects.get(iso=value[:2])
    except:
        return Country.objects.get(iso='FR')

def convert_abstract(value, model):
    """Convert string to a abstracted model"""
    return [model.objects.get_or_create(name=abstract,
                                        slug=slugify(abstract))[0]
            for abstract in value.split(',')]

CIVILITY_REVERSE = {'unknown': 0, 'mlle': 1,
                    'mme': 2, 'mr': 3, 'mlle, mr': 4,
                    'mme, mr': 5, 'mmes': 6, 'mrs': 7,
                    'ste': 0}

def convert_civility(value):
    """Convert string to civility"""
    if not value:
        return Profile.CIVILITY_CHOICES[0][0]
    else:
        return CIVILITY_REVERSE[value]


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
