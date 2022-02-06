from django import forms
from .models import StaffInfo

class DropdownDate(forms.DateInput):
    input_type = 'date'


class StaffInputForm(forms.ModelForm):
  class Meta:
    widgets = {'start_date': DropdownDate, 'end_date': DropdownDate}
    model = StaffInfo
    fields = "__all__"


class SearchFilterForm(forms.ModelForm):
  class Meta:
    model = StaffInfo
    fields = [
      'first_name',
      'last_name',
      'department',
      'job_title'
    ]
     