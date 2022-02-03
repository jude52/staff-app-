from dataclasses import fields
from re import template
from django.shortcuts import render
from django.template import context
from .models import StaffInfo
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .form import SearchFilterForm, StaffInputForm
from .filters import StaffFilter
from django.db.models import Q

class HomeTry(ListView):
    model = StaffInfo
    template_name = "/"



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
    form_class = StaffInputForm
 


class DeleteStaffMember(DeleteView):
    model = StaffInfo
    template_name = "staff/delete.html"
    success_url = "staff/input.html"

class UpdateStaffMember(UpdateView):
    model = StaffInfo
    template_name = "staff/update_info.html"
    form_class = StaffInputForm 
    success_url = "/"
 

def search_filter(request):
    staff= StaffInfo.objects.all()
    filter = StaffFilter(request.GET, queryset = staff)
    return render(request, "staff/filters.html", {'filter' : filter})


# class SearchResultsView(ListView):
#     model = StaffInfo
#     template_name = 'staff/input.html'

#     def get_queryset(self): # new
#         return StaffInfo.objects.filter(name__icontains='name')

# class SearchingForSearch(FormView):
#     model = StaffInfo
#     template_name = "staff/update_info.html"
#     form_class = SearchFilterForm
    


