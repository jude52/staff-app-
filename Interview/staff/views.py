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
# def home(request):
#     if 'q1' in request.GET:
#         q1= request.GET['q1']
#         searching = StaffInfo.objects.filter(title__icontains=q1)
#     else:
#         searching = StaffInfo.objects.all()

#     context = {"company": "NESCOLL"}
#     return render(request, "staff/home.html", context)

def home(request):
    context = {"company": "NESCOLL"}
    return render(request, "staff/home.html", context)

# def search(request):
#     if 'q1' in request.GET:
#         q1=request.GET['q1']
#         searching = StaffInfo.objects.filter(first_name__icontains=q1)
#     else:
#         searching =StaffInfo.objects.all()
#     return render(request, "staff/input.html", {'searching':searching})


class Input(ListView):
    model = StaffInfo
    template_name = "staff/input.html"
    queryset = StaffInfo.objects.order_by('last_name')
    #filter_me = queryset.filter(first_name__icontains='q')

    # def get_queryset(self):
    #     self.queryset = StaffInfo.objects.order_by('last_name')
    #     for name in 'last_names':
    #         look_up = self.queryset.filter(last_name__icontains=name.last_names)
    #     return look_up
    
 

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



# class SearchResultsView(ListView):
#     model = StaffInfo
#     template_name = 'staff/input.html'

    # def get_queryset(self):  
    #     context = super(Search, self).get_queryset(**kwargs)
    #     filter_set = StaffInfo.objects.all()
    #     if self.request.GET.get('q1'):
    #         first_name = self.request.GET.get('q1')
    #         filter_set = filter_set.filter(first_name__icontains=q1)

    #     context['first_name'] = StaffInfo.objects.all()
    #     return context

# class SearchingForSearch(FormView):
#     model = StaffInfo
#     template_name = "staff/update_info.html"
#     form_class = SearchFilterForm
    
# def filter_home(request):
#     qs = StaffInfo.objects.all()
#     first_name_search = request.GET.get('first_name_search') #name from input.html 
#     context = {
#         'queryset': qs 
# #     }
#     print(first_name_search)
#     return render(request, "", context)

 



class FilterInput(UpdateView):
    model = StaffInfo
    template_name = "staff/filter.html"
    #success_url = "staff/filter.html"