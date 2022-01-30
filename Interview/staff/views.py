from dataclasses import fields
from re import template
from django.shortcuts import render
from django.template import context
from .models import StaffInfo
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .form import StaffForm

# Create your views here.
def home(request):
    context = {"company": "NESCOLL"}
    return render(request, "staff/home.html", context)



 
class TestView(ListView):
    model = StaffInfo
    template_name = "staff/input.html"

class CreateStaffForm(CreateView):
    model = StaffInfo
    template_name = "staff/create_field.html"
    form_class = StaffForm

