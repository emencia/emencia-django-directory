"""Admin for emencia.django.directory Profile"""
import os
from datetime import datetime

from django import forms
from django.forms.util import ErrorList
from django.contrib import admin
from django.conf.urls.defaults import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.contrib.admin.views.main import ChangeList

from emencia.django.directory import settings
from emencia.django.directory.models import Profile
from emencia.django.directory.settings import MEDIA_URL
from emencia.django.directory.settings import SORL_THUMBNAIL_INSTALLED
from emencia.django.directory.workgroups import request_workgroups
from emencia.django.directory.workgroups import request_workgroups_profiles_pk


class ProfileChangeForm(forms.ModelForm):
    username = forms.RegexField(label=_('Username'), max_length=30, regex=r'^[-\w]+$', required=False,
                                help_text = _('Required. 30 characters or fewer. Alphanumeric characters only (letters, digits and underscores).'),
                                error_message = _('This value must contain only letters, numbers and underscores.'),
                                widget=admin.widgets.AdminTextInputWidget)
    first_name = forms.CharField(label=_('First name'), max_length=30, required=True,
                                 widget=admin.widgets.AdminTextInputWidget)
    last_name = forms.CharField(label=_('Last name'), max_length=30, required=True,
                                widget=admin.widgets.AdminTextInputWidget)
    password = forms.CharField(label=_('Password'), max_length=128, required=False,
                               widget=admin.widgets.AdminTextInputWidget)
    email = forms.EmailField(label=_('Email'), max_length=75, required=True,
                             widget=admin.widgets.AdminTextInputWidget)

    class Meta:
        model = Profile

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileChangeForm
    date_hierarchy = 'date_joined'
    list_display = ('get_picture', 'fullname', 'email', 'get_companies', 'country',
                    'get_sections', 'get_groups', 'is_active', 'is_staff',
                    'language', 'nature', 'get_categories', 'tags')
    list_filter = ('is_active', 'is_staff', 'civility', 'groups', 'language', 'nature',
                   'categories', 'sections', 'country', 'date_joined', 'visible')
    search_fields = ('first_name', 'last_name', 'email', 'city', 'address_1',
                     'address_2', 'postal_code', 'city', 'address_comments', 'tags', 'username',
                     'comments', 'phone', 'mobile', 'fax', 'function', 'reference',)
    filter_horizontal = ['categories', 'groups', 'user_permissions',
                         'sections', 'companies', 'competences']
    fieldsets = ((None, {'fields': ('civility', 'first_name', 'last_name', 'picture')}),
                 (_('Contact'), {'fields': ('email', 'email_alternative',
                                            'phone', 'mobile', 'fax', 'website',)}),
                 (_('Address'), {'fields': ('address_1', 'address_2', 'postal_code', 'city',
                                            'country', 'address_comments')}),
                 (_('Position'), {'fields': ('lat', 'lng'),
                                  'classes': ('collapse',),}),
                 (_('Personnal'), {'fields': ('language', 'birthdate', 'companies', 'function',
                                              'competences')}),
                 (_('User Access'), {'fields': ('username', 'password', 'is_active',
                                                'is_staff', 'is_superuser', 'last_login',
                                                'user_permissions', 'groups'),
                                'classes': ('collapse',),}),
                 (_('Classification'), {'fields': ('reference', 'nature',
                                                   'categories', 'sections', 'tags')}),
                 (_('Misc.'), {'fields': ('comments', 'visible', 'date_joined')}))
    prepopulated_fields = {'username': ('last_name', 'first_name', 'reference')}
    actions_on_top = False
    actions_on_bottom = True
    actions = ['create_mailinglist',]

    def get_actions(self, request):
        actions = super(ProfileAdmin, self).get_actions(request)
        if not settings.EDN_INSTALLED:
            del actions['create_mailinglist']
        return actions

    def fullname(self, contact):
        return contact.__unicode__()
    fullname.short_description = _('Full name')

    def get_picture(self, contact):
        if SORL_THUMBNAIL_INSTALLED and contact.picture:
            from sorl.thumbnail.main import DjangoThumbnail
            thumbnail = DjangoThumbnail(contact.picture, (75, 75))
            url = thumbnail.absolute_url
        else:
            img = 'male.jpg'
            if contact.civility in [1, 2, 6]:
                img = 'female.jpg'
            url = os.path.join(MEDIA_URL, 'img', img)
        return '<img src="%s" alt="%s" />' % (url, contact.__unicode__())
    get_picture.short_description = _('Picture')
    get_picture.allow_tags = True

    def get_groups(self, contact):
        return ', '.join([group.name for group in contact.groups.all()])
    get_groups.short_description = _('Groups')

    def get_categories(self, contact):
        return ', '.join([category.name for category in contact.categories.all()])
    get_categories.short_description = _('Categories')

    def get_sections(self, contact):
        return ', '.join([section.name for section in contact.sections.all()])
    get_sections.short_description = _('Sections')

    def get_companies(self, contact):
        return ', '.join([company.name for company in contact.companies.all()])
    get_companies.short_description = _('Companies')

    def queryset(self, request):
        queryset = super(ProfileAdmin, self).queryset(request)
        if not request.user.is_superuser:
            profiles_pk = request_workgroups_profiles_pk(request)
            queryset = queryset.filter(pk__in=profiles_pk)
        return queryset

    def save_model(admin, request, profile, form, change):
        workgroups = []
        if not profile.pk and not request.user.is_superuser:
            workgroups = request_workgroups(request)
        if profile.password and not profile.password.startswith('sha'):
            profile.set_password(profile.password)
        profile.save()
        for workgroup in workgroups:
            workgroup.profiles.add(profile)

    def create_mailinglist(self, request, queryset):
        """Create a mailing list from the profile list"""
        from emencia.django.newsletter.models import Contact
        from emencia.django.newsletter.models import MailingList
        from emencia.django.newsletter.settings import USE_WORKGROUPS
        from emencia.django.newsletter.utils.workgroups import request_workgroups as edn_request_workgroups
        
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

        if USE_WORKGROUPS:
            for workgroup in  edn_request_workgroups(request):
                workgroup.contacts.add(*subscribers)
                workgroup.mailinglists.add(new_mailing)

        self.message_user(request, _('%s succesfully created.') % new_mailing)
        return HttpResponseRedirect(reverse('admin:newsletter_mailinglist_change',
                                            args=[new_mailing.pk,]))
    create_mailinglist.short_description = _('Create a mailing list')

    def filtered_request_queryset(self, request):
        """Return queryset filtered by the admin list view"""
        cl = ChangeList(request, self.model, self.list_display,
                        self.list_display_links, self.list_filter,
                        self.date_hierarchy, self.search_fields,
                        self.list_select_related, self.list_per_page,
                        self.list_editable, self)
        return cl.get_query_set()

    def creation_mailinglist(self, request):
        """Create a mailing list form the filtered contacts"""
        return self.create_mailinglist(request, self.filtered_request_queryset(request))

    def get_urls(self):
        urls = super(ProfileAdmin, self).get_urls()
        my_urls = patterns('',
                           url(r'^create_mailinglist/$', self.creation_mailinglist,
                               name='directory_profile_create_mailinglist'),
                           )
        return my_urls + urls

