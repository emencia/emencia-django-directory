"""Models for emencia.django.directory"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings 
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from tagging.fields import TagField

from emencia.django.countries.models import Country
from emencia.django.directory.managers import CompanyManager
from emencia.django.directory.managers import ProfileManager
from emencia.django.directory.settings import CUSTOM_CIVILITIES

class AbstractCategory(models.Model):
    """Abstract Model for categorization"""
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    slug = models.SlugField(_('slug'), max_length=255,
                            unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True

class Category(AbstractCategory):
    """Category Model"""

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

class Nature(AbstractCategory):
    """Nature Model"""

    class Meta:
        verbose_name = _('nature')
        verbose_name_plural = _('natures')

class Section(AbstractCategory):
    """Section Model"""

    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')

class FieldOfCompetence(AbstractCategory):
    """Field of competence Model"""

    class Meta:
        verbose_name = _('field of competence')
        verbose_name_plural = _('fields of competences')

class Competence(AbstractCategory):
    """Competence Model"""
    field_of_competence = models.ForeignKey(FieldOfCompetence,
                                            verbose_name=_('field of competence'))
    
    class Meta:
        verbose_name = _('competence')
        verbose_name_plural = _('competences')


class Company(AbstractCategory):
    """Company Model"""
    picture = models.ImageField(_('logo'), upload_to='logos',
                                blank=True, null=True)
    description_additional = models.TextField(_('additional description'),
                                              blank=True)
    
    # Contact
    phone = models.CharField(_('phone'), max_length=40, blank=True)
    fax = models.CharField(_('fax'), max_length=40, blank=True)
    email = models.EmailField(_('e-mail address'), blank=True)
    website = models.CharField(_('website'), max_length=255,
                               blank=True)

    # Address
    address_1 = models.TextField(_('address 1'), blank=True)
    address_2 = models.TextField(_('address 2'), blank=True)
    address_comments = models.TextField(_('address comments'), blank=True)
    postal_code = models.CharField(_('postal code'), max_length=20, blank=True)
    city = models.CharField(_('city'), max_length=255, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('country'))
    lat = models.CharField(_('latitude'), max_length=30, blank=True)
    lng = models.CharField(_('longitude'), max_length=30, blank=True)    

    # Internal classification
    reference = models.CharField(_('reference'), max_length=255, blank=True)    
    nature = models.ForeignKey(Nature, verbose_name=_('nature'),
                               null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name=_('categories'),
                                        null=True, blank=True)
    sections = models.ManyToManyField(Section, verbose_name=_('sections'),
                                      null=True, blank=True)
    tags = TagField(_('tags'), blank=True)
    comments = models.TextField(_('comments'), blank=True)

    # Meta Data
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    modification_date = models.DateTimeField(_('modification date'), auto_now=True)
    visible = models.BooleanField(_('visible'), default=True)
    
    objects = CompanyManager()

    @models.permalink
    def get_absolute_url(self):
        return ('directory_company_detail', (self.slug,))

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')

class Profile(User):
    """Profile Model"""

    CIVILITY_CHOICES = ((0, _('unknown')),
                        (1, _('mlle')),
                        (2, _('mme')),
                        (3, _('mr')),
                        (4, _('mlle, mr')),
                        (5, _('mme, mr')),
                        (6, _('mmes')),
                        (7, _('mrs')),
                        ) + CUSTOM_CIVILITIES

    # Civility
    civility = models.IntegerField(_('civility'), choices=CIVILITY_CHOICES,
                                   default=0)
    picture = models.ImageField(_('picture'), upload_to='trombi',
                                blank=True, null=True)
    # Contact
    phone = models.CharField(_('phone'), max_length=40, blank=True)
    mobile = models.CharField(_('mobile'), max_length=40, blank=True)
    fax = models.CharField(_('fax'), max_length=40, blank=True)
    email_alternative = models.EmailField(_('alternative e-mail address'),
                                          blank=True)
    website = models.CharField(_('website'), max_length=255,
                               blank=True)

    # Address
    address_1 = models.TextField(_('address 1'), blank=True)
    address_2 = models.TextField(_('address 2'), blank=True)
    address_comments = models.TextField(_('address comments'), blank=True)
    postal_code = models.CharField(_('postal code'), max_length=20, blank=True)
    city = models.CharField(_('city'), max_length=255, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('country'))
    lat = models.CharField(_('latitude'), max_length=30, blank=True)
    lng = models.CharField(_('longitude'), max_length=30, blank=True)

    # Personnal info
    language = models.CharField(_('language'), max_length=10, blank=True,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGES[0][0])
    birthdate = models.DateField(_('birthdate'), help_text=_('yyyy-mm-dd format'),
                                 blank=True, null=True)
    companies = models.ManyToManyField(Company, verbose_name=_('companies'),
                                       null=True, blank=True)
    function = models.CharField(_('function'), max_length=255, blank=True)
    competences = models.ManyToManyField(Competence, verbose_name=_('competences'),
                                         null=True, blank=True)

    # Internal classification
    reference = models.CharField(_('reference'), max_length=255, blank=True)
    nature = models.ForeignKey(Nature, verbose_name=_('nature'),
                               null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name=_('categories'),
                                        null=True, blank=True)
    sections = models.ManyToManyField(Section, verbose_name=_('sections'),
                                      null=True, blank=True)
    tags = TagField(_('tags'), blank=True)
    comments = models.TextField(_('comments'), blank=True)

    # Meta Data
    modification_date = models.DateTimeField(_('modification date'), auto_now=True)
    visible = models.BooleanField(_('visible'), default=True)
    
    objects = ProfileManager()
    
    def __unicode__(self):
        return '%s %s %s' % (self.get_civility_display(),
                             self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ('directory_profile_detail', (self.username,))

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
        ordering = ('last_name', 'first_name')

class WorkGroup(models.Model):
    """WorkGroup Model"""
    name = models.CharField(_('name'), max_length=255)
    group = models.ForeignKey(Group, verbose_name=_('permissions group'),
                              related_name='directory_workgroup_group')

    categories = models.ManyToManyField(Category, verbose_name=_('categories'),
                                        blank=True, null=True)
    natures = models.ManyToManyField(Nature, verbose_name=_('natures'),
                                     blank=True, null=True)
    sections = models.ManyToManyField(Section, verbose_name=_('sections'),
                                      blank=True, null=True)
    companies = models.ManyToManyField(Company, verbose_name=_('companies'),
                                       blank=True, null=True)
    profiles = models.ManyToManyField(Profile, verbose_name=_('profiles'),
                                      blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('workgroup')
        verbose_name_plural = _('workgroups')

    

