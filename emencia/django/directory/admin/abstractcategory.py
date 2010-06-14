"""Admin for emencia.django.directory AbstractCategory based Models"""
from django.contrib import admin
from django.utils.translation import ugettext as _

from emencia.django.directory.models import Category
from emencia.django.directory.models import Nature
from emencia.django.directory.models import Section
from emencia.django.directory.models import Company
from emencia.django.directory.models import Profile
from emencia.django.directory.workgroups import request_workgroups
from emencia.django.directory.workgroups import request_workgroups_abstract_categories_pk

WORKGROUP_RELATIONS = {Category: 'categories',
                       Nature: 'natures',
                       Section: 'sections',
                       Company: 'companies',
                       Profile: 'profiles'}

class AbstractCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug', 'description')
    fieldsets = ((None, {'fields': ('name', 'description')}),
                 (None, {'fields': ('slug',)}),)
    prepopulated_fields = {'slug': ('name',)}
    actions_on_top = False
    actions_on_bottom = True

    def queryset(self, request):
        queryset = super(AbstractCategoryAdmin, self).queryset(request)
        if not request.user.is_superuser:            
            relation = WORKGROUP_RELATIONS[self.model]
            abstract_categories_pk = request_workgroups_abstract_categories_pk(request, relation)
            queryset = queryset.filter(pk__in=abstract_categories_pk)
        return queryset
            
    def save_model(self, request, abstract_category, form, change):
        workgroups = []
        if not abstract_category.pk and not request.user.is_superuser:
            workgroups = request_workgroups(request)
        abstract_category.save()
        relation = WORKGROUP_RELATIONS[self.model]
        for workgroup in workgroups:
            getattr(workgroup, relation).add(abstract_category)
