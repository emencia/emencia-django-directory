"""Admin for emencia.django.newsletter"""
from django.contrib import admin
from django.conf import settings

from emencia.django.directory import settings
from emencia.django.directory.models import Category
from emencia.django.directory.models import Nature
from emencia.django.directory.models import Company
from emencia.django.directory.models import Profile
from emencia.django.directory.admin.profile import ProfileAdmin
from emencia.django.directory.admin.abstractcategory import AbstractCategoryAdmin

admin.site.register(Category, AbstractCategoryAdmin)
admin.site.register(Nature, AbstractCategoryAdmin)
admin.site.register(Company, AbstractCategoryAdmin)

admin.site.register(Profile, ProfileAdmin)
