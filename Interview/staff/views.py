from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"company": "NESCOLL"}
    return render(request, "staff/home.html", context)