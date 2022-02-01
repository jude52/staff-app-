import django_filters 
from .models import StaffInfo


class StaffFilter(django_filters.FilterSet):
    class Meta:
        model = StaffInfo
        fields =  {'first_name': ['icontains'],
		          'last_name': ['exact'],
                  'department': ['gt'],
                 }