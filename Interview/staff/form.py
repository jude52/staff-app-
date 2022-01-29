from django import forms
from .models import StaffInfo

class StaffForm(forms.ModelForm):
  class Meta:
    model = StaffInfo
    fields = '__all__'