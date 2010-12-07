"""ModelAdmin for WorkGroup"""
from django.contrib import admin
from django.utils.translation import ugettext as _

class WorkGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'profiles_length',
                    'companies_length', 'categories_length',
                    'natures_length', 'sections_length')
                    
    fieldsets = ((None, {'fields': ('name', 'group')}),
                 (None, {'fields': ('profiles', 'companies', 'categories',
                                    'natures', 'sections')}),
                 )
    filter_horizontal = ['profiles', 'companies', 'categories',
                         'natures', 'sections']
    actions_on_top = False
    actions_on_bottom = True

    def profiles_length(self, workgroup):
        return workgroup.profiles.count()
    profiles_length.short_description = _('Profiles length')

    def companies_length(self, workgroup):
        return workgroup.companies.count()
    companies_length.short_description = _('Companies length')

    def categories_length(self, workgroup):
        return workgroup.categories.count()
    categories_length.short_description = _('Categories length')

    def natures_length(self, workgroup):
        return workgroup.natures.count()
    natures_length.short_description = _('Natures length')

    def sections_length(self, workgroup):
        return workgroup.sections.count()
    sections_length.short_description = _('Sections length')
