"""Admin for emencia.django.directory"""
from django.contrib import admin
from django.conf import settings

from emencia.django.directory import settings
from emencia.django.directory.models import Category
from emencia.django.directory.models import Nature
from emencia.django.directory.models import Section
from emencia.django.directory.models import Company
from emencia.django.directory.models import Profile
from emencia.django.directory.models import WorkGroup
from emencia.django.directory.models import Competence
from emencia.django.directory.models import FieldOfCompetence
from emencia.django.directory.settings import USE_WORKGROUPS
from emencia.django.directory.admin.company import CompanyAdmin
from emencia.django.directory.admin.profile import ProfileAdmin
from emencia.django.directory.admin.workgroup import WorkGroupAdmin
from emencia.django.directory.admin.competence import CompetenceAdmin
from emencia.django.directory.admin.competence import FieldOfCompetenceAdmin
from emencia.django.directory.admin.abstractcategory import AbstractCategoryAdmin

admin.site.register(Nature, AbstractCategoryAdmin)
admin.site.register(Section, AbstractCategoryAdmin)
admin.site.register(Category, AbstractCategoryAdmin)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(FieldOfCompetence, FieldOfCompetenceAdmin)

if USE_WORKGROUPS:
    admin.site.register(WorkGroup, WorkGroupAdmin)
