import django_filters 
from .models import StaffInfo


class StaffFilter(django_filters.FilterSet):
    class Meta:
        model = StaffInfo
        fields =  {'first_name': ['istartswith'],
		          'last_name': ['istartswith'],
                  'department': ['icontains'],
                  'job_title': ['icontains']
                 }