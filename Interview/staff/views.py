from dataclasses import fields
from re import search, template
from turtle import title
from django.shortcuts import render
from django.template import context
from .models import StaffInfo
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .form import SearchFilterForm, StaffInputForm
from .filters import StaffFilter
from django.db.models import Q

from django.contrib import messages
from django.core.paginator import Paginator

from django.core import serializers
from django.http import JsonResponse

# Create your views here.
# def home(request):
#     if 'q1' in request.GET:
#         q1= request.GET['q1']
#         searching = StaffInfo.objects.filter(title__icontains=q1)
#     else:
#         searching = StaffInfo.objects.all()

#     context = {"company": "NESCOLL"}
#     return render(request, "staff/home.html", context)

def home(request):
    if 'q1' in request.GET:
        q1=request.GET['q1']
        searching = StaffInfo.objects.filter(first_name__icontains=q1)
        print(searching)
    else:
        searching =StaffInfo.objects.all()
    # Pagintion
    # paginator=Paginator(posts,2)
    # page_number=request.GET.get('page')
    # posts_obj=paginator.get_page(page_number)

    return render(request,"", {'filter':filter})

class Input(ListView):
    model = StaffInfo
    template_name = "staff/input.html"

    # def search_filter(request):
    #     staff= StaffInfo.objects.all()
    #     filter = StaffFilter(request.GET, queryset = staff)
    #     return render(request, "/", {'filter' : filter})
  

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
 



# def search_input(request):
#     staff1= StaffInfo.objects.all()
#     filter1 = StaffFilter(request.GET, queryset = staff1)
#     return render(request, "staff/input.html", {'filter' : filter1})

# class FilterInput(UpdateView):
#     model = StaffInfo
#     template_name = "staff/input.html"

# class SearchResultsView(ListView):
#     model = StaffInfo
#     template_name = 'staff/input.html'

#     def get_queryset(self): # new
#         return StaffInfo.objects.filter(name__icontains='name')

# class SearchingForSearch(FormView):
#     model = StaffInfo
#     template_name = "staff/update_info.html"
#     form_class = SearchFilterForm
    
def filter_home(request):
    qs = StaffInfo.objects.all()
    first_name_search = request.GET.get('first_name_search') #name from input 
    context = {
        'queryset': qs 
    }
    print(first_name_search)
    return render(request, "", context)
