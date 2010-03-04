========================
Emencia Django Directory
========================

Emencia.django.directory try to resolve many problems in a django project :

 - The lack of profile in django.contrib.auth
 - The ugly integration in the admin app

And emencia.django.directory try to be :

 - A generic directory app, easily customizable
 - A complement of django.contrib.auth
 - A complement of emencia.django.newsletter

The concept is still not fixed, it will evolve and suggestions are welcome.

Installation
============

You could retrieve the last sources from http://github.com/Fantomas42/emencia-django-directory and running the installation script ::
    
  $> python setup.py install

or use pip ::

  $> pip install -e git://github.com/Fantomas42/emencia-django-directory.git#egg=emencia.django.directory

Dependancies
------------

Emencia.django.directory has several dependancies to django applications.

  * tagging
  * emencia.django.countries
  * sorl.thumbnail (optionnal)

Applications
------------

Then register this following applications in the INSTALLED_APPS section of your project's settings. ::

  >>> INSTALLED_APPS = (
  ...   'django.contrib.auth',
  ...   'django.contrib.contenttypes',
  ...   'django.contrib.admin',
  ...   'tagging',
  ...   'sorl.thumbnail',
  ...   'emencia.django.countries',
  ...   'emencia.django.directory',)


Template Context Processors
---------------------------

Add the following template context processors if not already present. ::

  >>> TEMPLATE_CONTEXT_PROCESSORS = (
  >>>      'django.core.context_processors.auth',
  >>>      'django.core.context_processors.i18n',
  >>>      'django.core.context_processors.request',
  >>>      'django.core.context_processors.media',
  >>>      'emencia.django.directory.context_processors.media',
  >>>	)

Urls
----

In your project urls.py adding this following line to include the directory's urls. ::

  >>> url(r'^directory/', include('emencia.django.directory.urls')),

Media Files
-----------

You have to make a symbolic link from emencia/django/directory/media/ directory to your media directory or make a copy named **edd**,
but if want to change this value, define DIRECTORY_MEDIA_URL in the settings.py as appropriate.

Don't forget to serve this url.

