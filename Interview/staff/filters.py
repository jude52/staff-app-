import django_filters 
from .models import StaffInfo


class StaffFilter(django_filters.FilterSet):
    class Meta:
        model = StaffInfo
        fields =  {'first_name': ['icontains'],
		          'last_name': ['icontains'],
                  'department': ['icontains'],
                  'job_title': ['icontains']
                 }