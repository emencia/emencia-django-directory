"""Utils for workgroups"""
from emencia.django.directory.models import WorkGroup

def request_workgroups(request):
    return WorkGroup.objects.filter(group__in=request.user.groups.all())

def request_workgroups_profiles_pk(request):
    profiles = []
    for workgroup in request_workgroups(request):
        profiles.extend([p.pk for p in workgroup.profiles.all()])
    return set(profiles)

def request_workgroups_abstract_categories_pk(request, relation):
    abstract_categories = []
    for workgroup in request_workgroups(request):
        abstract_categories.extend([ac.pk for ac in getattr(workgroup, relation).all()])
    return set(abstract_categories)
