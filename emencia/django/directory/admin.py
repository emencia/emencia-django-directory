"""Admin for emencia.django.directory"""
from django.contrib import admin
from django.utils.translation import ugettext as _

from emencia.django.directory.models import Category
from emencia.django.directory.models import Nature
from emencia.django.directory.models import Company
from emencia.django.directory.models import Country
from emencia.django.directory.models import Profile

class AbstractCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    fieldsets = ((None, {'fields': ('name', 'description')}),
                 (None, {'fields': ('slug',)}),)
    prepopulated_fields = {'slug': ('name',)}
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(Category, AbstractCategoryAdmin)
admin.site.register(Nature, AbstractCategoryAdmin)
admin.site.register(Company, AbstractCategoryAdmin)
admin.site.register(Country, AbstractCategoryAdmin)

admin.site.register(Profile)
