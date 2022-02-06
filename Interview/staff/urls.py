from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("staff/input.html", views.Input.as_view(), name='results'),
    path("staff/create_field.html", views.CreateStaffForm.as_view(), name='create_form'),
    path("staff/<pk>/delete/", views.DeleteStaffMember.as_view(), name='delete'),
    path("staff/<pk>/update/", views.UpdateStaffMember.as_view(), name='update'),
   # path("staff/filter.html/", views.FilterInput.as_view(), name="filter"),
]