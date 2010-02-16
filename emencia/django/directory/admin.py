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

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    list_display_links = ('civility', 'first_name', 'last_name')
    list_display = ('civility', 'first_name', 'last_name',
                    'email', 'company', 'country', 'get_groups',
                    'language', 'nature', 'get_categories', 'tags')
    list_filter = ('civility', 'groups', 'language', 'nature', 'categories',
                   'country', 'creation_date')
    search_fields = ('first_name', 'last_name', 'email', 'company', 'city', 'address_1',
                     'address_2', 'postal_code', 'city', 'address_comments', 'tags',
                     'comments', 'phone', 'mobile', 'fax', 'function', 'reference', 'slug')
    filter_horizontal = ['categories', 'groups']
    fieldsets = ((None, {'fields': ('civility', 'first_name', 'last_name',)}),
                 (_('Contact'), {'fields': ('email', 'phone', 'mobile', 'fax')}),
                 (_('Address'), {'fields': ('address_1', 'address_2', 'postal_code', 'city',
                                            'country', 'address_comments')}),                 
                 (_('Personnal'), {'fields': ('language', 'birthdate', 'company', 'function',)}),
                 (_('Classification'), {'fields': ('reference', 'nature',
                                                   'categories', 'tags', 'groups')}),
                 (_('Misc.'), {'fields': ('comments', 'slug',)}))
    actions_on_top = False
    actions_on_bottom = True

    def get_groups(self, contact):
        return ', '.join([group.name for section in contact.groups.all()])
    get_groups.short_description = _('Groups')

    def get_categories(self, contact):
        return ', '.join([category.name for category in contact.categories.all()])
    get_categories.short_description = _('Categories')


admin.site.register(Profile, ProfileAdmin)

