from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("staff/input.html", views.Input.as_view(), name='input'),
    path("staff/create_field.html", views.CreateStaffForm.as_view(), name='create_form'),
   # path('<pk>/delete.html/', views.DeleteStaff.as_view()),
    # path("staff/delete.html/", views.DeleteStaff.as_view(), name='delete'),
    path("staff/<pk>/delete/", views.DeleteStaffMember.as_view(), name='delete1'),
    path("staff/<pk>/update/", views.UpdateStaffMember.as_view(), name='update')
]