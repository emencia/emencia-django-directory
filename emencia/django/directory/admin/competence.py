"""Admin for emencia.django.directory Competence"""
from django.contrib import admin
from django.utils.translation import ugettext as _

from emencia.django.directory.models import Competence

class CompetenceInline(admin.TabularInline):
    model = Competence
    prepopulated_fields = {'slug': ('name',)}

class FieldOfCompetenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug', 'description')
    inlines = (CompetenceInline,)
    fieldsets = ((None, {'fields': ('name', 'description')}),
                 (None, {'fields': ('slug',)}),)
    prepopulated_fields = {'slug': ('name',)}
    actions_on_top = False
    actions_on_bottom = True

class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'field_of_competence', 'slug')
    list_filter = ('field_of_competence',)
    search_fields = ('name', 'slug', 'description')
    fieldsets = ((None, {'fields': ('field_of_competence',
                                    'name', 'description')}),
                 (None, {'fields': ('slug',)}),)
    prepopulated_fields = {'slug': ('name',)}
    actions_on_top = False
    actions_on_bottom = True

