from dataclasses import fields
from django.shortcuts import render
from django.template import context
from .models import StaffInfo
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
def home(request):
    context = {"company": "NESCOLL"}
    return render(request, "staff/home.html", context)

 
class TestView(ListView):
    model = StaffInfo
    template_name = "staff/input.html"

class CreateTestView(CreateView):
    model = StaffInfo
    template_name = "staff/create_field.html"
    fields = [
       'first_name', 
        'last_name', 'department', 'job_title', 'start_date', 'end_date'

    ]