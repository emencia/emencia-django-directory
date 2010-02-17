"""Admin for emencia.django.directory AbstractCategory based Models"""
from django.contrib import admin
from django.utils.translation import ugettext as _

class AbstractCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    fieldsets = ((None, {'fields': ('name', 'description')}),
                 (None, {'fields': ('slug',)}),)
    prepopulated_fields = {'slug': ('name',)}
    actions_on_top = False
    actions_on_bottom = True

