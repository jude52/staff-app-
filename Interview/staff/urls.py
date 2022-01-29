from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("staff/input.html", views.TestView.as_view(), name='input'),
    path("staff/create_field.html", views.CreateTestView.as_view(), name='create'),
    
]