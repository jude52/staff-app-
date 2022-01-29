from dataclasses import fields
from django.shortcuts import render
from django.template import context
from .models import StaffInfo
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#from .forms import 

# Create your views here.
def home(request):
    context = {"company": "NESCOLL"}
    return render(request, "staff/home.html", context)

def CreateField(request):
    if method.request =="POST":
        CreateNew = StaffInfo()
        CreateNew.first_name = request.POST["first_name"]
        CreateNew.last_name = request.POST["last_name"]
        CreateNew.department = request.POST["department"]
        CreateNew.job_title = request.POST["job_title"]
        CreateNew.start_date = request.POST["start_date"]
        CreateNew.end_date = request.POST["end_date"]
        CreateNew.save()
    return render(request, "staff/create_field.html")

 
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