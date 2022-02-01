from dataclasses import fields
from re import template
from django.shortcuts import render
from django.template import context
from .models import StaffInfo
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .form import StaffForm
from .filters import StaffFilter

# Create your views here.
def home(request):
    context = {"company": "NESCOLL"}
    return render(request, "staff/home.html", context)



 
class Input(ListView):
    model = StaffInfo
    template_name = "staff/input.html"

class CreateStaffForm(CreateView):
    model = StaffInfo
    template_name = "staff/create_field.html"
    form_class = StaffForm

# class DeleteStaff(ListView):
#     model = StaffInfo
#     template_name = "staff/delete.html"

class DeleteStaffMember(DeleteView):
    model = StaffInfo
    template_name = "staff/delete.html"
    success_url = "/"

class UpdateStaffMember(UpdateView):
    model = StaffInfo
    template_name = "staff/update_info.html"
    form_class = StaffForm 
    success_url = "/"

def search_filter(request):
	staff= StaffInfo.objects.all()
	filter = StaffFilter(request.GET, queryset = staff)
	return render(request, 'staff/filters.html', {'filter' : filter})
