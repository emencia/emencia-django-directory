"""Views for emencia.django.directory Profile"""
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from emencia.django.directory.models import Company
from emencia.django.directory.models import Profile
from emencia.django.directory.settings import PAGINATION


def view_company_profile_list(request, slug):
    """Return profiles for a company"""
    company = get_object_or_404(Company, slug=slug)
    return object_list(request, paginate_by=PAGINATION,
                       queryset=Profile.objects.published().filter(companies=company))
