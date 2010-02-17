"""Admin for emencia.django.directory Profile"""
from datetime import datetime

from django import forms
from django.forms.util import ErrorList
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect

from emencia.django.directory import settings
from emencia.django.directory.models import Profile

class ProfileChangeForm(forms.ModelForm):
    username = forms.RegexField(label=_('Username'), max_length=30, regex=r'^\w+$', required=False,
                                help_text = _('Required. 30 characters or fewer. Alphanumeric characters only (letters, digits and underscores).'),
                                error_message = _('This value must contain only letters, numbers and underscores.'))
    first_name = forms.CharField(label=_('First name'), max_length=30, required=True)
    last_name = forms.CharField(label=_('Last name'), max_length=30, required=True)
    password = forms.CharField(label=_('Password'), max_length=128, required=False)
    email = forms.EmailField(label=_('Email'), max_length=75, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and not password:
            self._errors['password'] = ErrorList([_('You must define a password for your username.')])
        if password and not username:
            self._errors['username'] = ErrorList([_('You must define an username if you set a password.')])
        
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(_('A user with that username already exists.'))
    
    class Meta:
        model = Profile

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileChangeForm
    date_hierarchy = 'date_joined'
    list_display = ('fullname', 'email', 'company', 'country', 'get_sections', 'get_groups',
                    'is_active', 'is_staff', 'language', 'nature', 'get_categories', 'tags')
    list_filter = ('is_active', 'is_staff', 'civility', 'groups', 'language', 'nature',
                   'categories', 'country', 'date_joined', 'visible')
    search_fields = ('first_name', 'last_name', 'email', 'company', 'city', 'address_1',
                     'address_2', 'postal_code', 'city', 'address_comments', 'tags', 'username',
                     'comments', 'phone', 'mobile', 'fax', 'function', 'reference',)
    filter_horizontal = ['categories', 'groups', 'user_permissions', 'sections',]
    fieldsets = ((None, {'fields': ('civility', 'first_name', 'last_name',)}),
                 (_('Contact'), {'fields': ('email', 'phone', 'mobile', 'fax')}),
                 (_('Address'), {'fields': ('address_1', 'address_2', 'postal_code', 'city',
                                            'country', 'address_comments')}),
                 (_('Position'), {'fields': ('lat', 'lng'),
                                  'classes': ('collapse',),}),
                 (_('Personnal'), {'fields': ('language', 'birthdate', 'company', 'function',)}),
                 (_('User Access'), {'fields': ('username', 'password', 'is_active',
                                                'is_staff', 'is_superuser', 'last_login',
                                                'user_permissions', 'groups'),
                                'classes': ('collapse',),}),
                 (_('Classification'), {'fields': ('reference', 'nature',
                                                   'categories', 'sections', 'tags')}),
                 (_('Misc.'), {'fields': ('comments', 'visible', 'date_joined')}))
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

    def get_sections(self, contact):
        return ', '.join([section.name for section in contact.sections.all()])
    get_sections.short_description = _('Sections')
    
    def save_model(admin, request, profile, form, change):
        if not profile.password.startswith('sha'):
            profile.set_password(profile.password)
        profile.save()                                            

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


