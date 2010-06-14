"""Admin for emencia.django.directory Company"""
import os
from django.contrib import admin
from django.utils.translation import ugettext as _

from emencia.django.directory.settings import MEDIA_URL
from emencia.django.directory.settings import SORL_THUMBNAIL_INSTALLED

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('get_picture', 'name', 'website', 'country',
                    'get_sections', 'nature', 'get_categories', 'tags')
    list_filter = ('nature', 'categories', 'sections', 'country', 'visible',)
    search_fields = ('name', 'description', 'description_additional',
                     'reference', 'phone', 'fax', 'email', 'website',
                     'address_1', 'address_2', 'address_comments', 'postal_code',
                     'city', 'phone', 'fax', 'email', 'website', 'tags', 'comments')
    filter_horizontal = ['categories', 'sections']
    fieldsets = ((None, {'fields': ('name', 'picture',)}),
                 (_('Description'), {'fields': ('description', 'description_additional')}),                 
                 (_('Contact'), {'fields': ('phone', 'fax', 'email', 'website',)}),
                 (_('Address'), {'fields': ('address_1', 'address_2', 'postal_code', 'city',
                                            'country', 'address_comments')}),
                 (_('Position'), {'fields': ('lat', 'lng'),
                                  'classes': ('collapse',),}),
                 (_('Classification'), {'fields': ('reference', 'nature',
                                                   'categories', 'sections', 'tags')}),
                 (_('Misc.'), {'fields': ('comments', 'visible', 'slug')}))
    prepopulated_fields = {'slug': ('name', 'reference')}
    actions_on_top = False
    actions_on_bottom = True

    def get_picture(self, company):
        if SORL_THUMBNAIL_INSTALLED and company.picture:
            from sorl.thumbnail.main import DjangoThumbnail
            thumbnail = DjangoThumbnail(company.picture, (75, 75))
            url = thumbnail.absolute_url
        else:
            img = 'company.jpg'
            url = os.path.join(MEDIA_URL, 'img', img)
        return '<img src="%s" alt="%s" />' % (url, company.__unicode__())
    get_picture.short_description = _('Picture')
    get_picture.allow_tags = True


    def get_categories(self, contact):
        return ', '.join([category.name for category in contact.categories.all()])
    get_categories.short_description = _('Categories')

    def get_sections(self, contact):
        return ', '.join([section.name for section in contact.sections.all()])
    get_sections.short_description = _('Sections')
