from django import forms
from .models import StaffInfo

class DropdownDate(forms.DateInput):
    input_type = 'date'



class StaffForm(forms.ModelForm):
  class Meta:
    widgets = {'start_date': DropdownDate, 'end_date': DropdownDate}
    model = StaffInfo
    fields = "__all__"
   