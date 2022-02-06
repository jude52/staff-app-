from dataclasses import fields
from re import search, template
from turtle import title
from django.http import request
from django.shortcuts import render
from django.template import context
from .models import StaffInfo
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .form import SearchFilterForm, StaffInputForm
from .filters import StaffFilter
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.
 

def home(request):
    context = {
        "company": "NESCOLL",
        "Entry": "Entry",
        "Results": "Results"
    }
    return render(request, "staff/home.html", context)

class Input(ListView):
    model = StaffInfo
    template_name = "staff/input.html"
    queryset = StaffInfo.objects.order_by('last_name')
 
 
class CreateStaffForm(CreateView):
    model = StaffInfo
    template_name = "staff/create_field.html"
    form_class = StaffInputForm
    success_url = "/"
 
class DeleteStaffMember(DeleteView):
    model = StaffInfo
    template_name = "staff/delete.html"
    success_url = "/"

class UpdateStaffMember(UpdateView):
    model = StaffInfo
    template_name = "staff/update_info.html"
    form_class = StaffInputForm 
    success_url = "/"
<<<<<<< HEAD

# def search_filter(request):
# 	staff= StaffInfo.objects.all()
# 	filter = StaffFilter(request.GET, queryset = staff)
# 	return render(request, 'staff/filters.html', {'filter' : filter})
# =======
 
>>>>>>> develop
