from django.urls import path
from . import views

urlpatterns = [
    path('manage-staff/', views.manage_staff, name='manage_staff'),
    path('assign-role-section/<int:staff_id>/', views.assign_role_section, name='assign_role_section'),
    path('edit-staff/<int:staff_id>/', views.edit_staff, name='edit_staff'),
    path('delete-staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),

]
