from django.contrib.auth.models import User
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = StaffInfo
        fields = ['first_name', 'last_name', 'deapartment', 'job_title' ]