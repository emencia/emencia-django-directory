"""Admin for emencia.django.directory"""
from datetime import datetime

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect

from emencia.django.directory import settings
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

class CountryAdmin(admin.ModelAdmin):
    search_fields = ('printable_name', 'name', 'iso', 'iso3')
    list_display = ('printable_name', 'name', 'iso', 'iso3', 'numcode','level')
    ordering = ('printable_name',)
    fieldsets = ((None, {'fields': ('printable_name', 'name')}),
                 (_('References'), {'fields': ('iso', 'iso3', 'numcode')}),
                 (None, {'fields': ('level',)}),)
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(Country, CountryAdmin)


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    list_display = ('fullname', 'email', 'company', 'country', 'get_groups',
                    'language', 'nature', 'get_categories', 'tags')
    list_filter = ('civility', 'groups', 'language', 'nature', 'categories',
                   'country', 'creation_date', 'visible')
    search_fields = ('first_name', 'last_name', 'email', 'company', 'city', 'address_1',
                     'address_2', 'postal_code', 'city', 'address_comments', 'tags',
                     'comments', 'phone', 'mobile', 'fax', 'function', 'reference', 'slug')
    filter_horizontal = ['categories', 'groups']
    fieldsets = ((None, {'fields': ('civility', 'first_name', 'last_name',)}),
                 (_('Contact'), {'fields': ('email', 'phone', 'mobile', 'fax')}),
                 (_('Address'), {'fields': ('address_1', 'address_2', 'postal_code', 'city',
                                            'country', 'address_comments')}),
                 (_('Position'), {'fields': ('lat', 'lng')}),
                 (_('Personnal'), {'fields': ('language', 'birthdate', 'company', 'function',)}),
                 (_('Classification'), {'fields': ('reference', 'nature',
                                                   'categories', 'tags', 'groups')}),
                 (_('Misc.'), {'fields': ('comments', 'slug', 'visible')}))
    prepopulated_fields = {'slug': ('first_name', 'last_name', 'language',)}
    actions_on_top = False
    actions_on_bottom = True
    actions = ['make_mailinglist',]

    def get_actions(self, request):
        actions = super(ProfileAdmin, self).get_actions(request)
        if not settings.EDN_INSTALLED:
            del actions['make_mailinglist']
        return actions

    def fullname(self, contact):
        return contact.__unicode__()
    fullname.short_description = _('Full name')

    def get_groups(self, contact):
        return ', '.join([group.name for section in contact.groups.all()])
    get_groups.short_description = _('Groups')

    def get_categories(self, contact):
        return ', '.join([category.name for category in contact.categories.all()])
    get_categories.short_description = _('Categories')

    def make_mailinglist(self, request, queryset):
        """Create a mailing list from the profile list"""
        from emencia.django.newsletter.models import Contact
        from emencia.django.newsletter.models import MailingList
        subscribers = []
        for profile in queryset:
            contact, created = Contact.objects.get_or_create(email=profile.email,
                                                             defaults={'first_name': profile.first_name,
                                                                       'last_name': profile.last_name,
                                                                       'tags': profile.tags,
                                                                       'content_object': profile})
            subscribers.append(contact)
        when = str(datetime.now()).split('.')[0]
        new_mailing = MailingList(name=_('New mailinglist at %s') % when,
                                  description=_('New mailing list created from admin/directory %s') % when)
        new_mailing.save()
        for subscriber in subscribers:
            new_mailing.subscribers.add(subscriber)
        new_mailing.save()
        
        self.message_user(request, _('%s succesfully created.') % new_mailing)
        return HttpResponseRedirect(reverse('admin:newsletter_mailinglist_change',
                                            args=[new_mailing.pk,]))
    make_mailinglist.short_description = _('Create a mailing list')

admin.site.register(Profile, ProfileAdmin)

