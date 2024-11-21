from django.urls import path
from . import views
from .views import login_view, logout_view

urlpatterns = [
    path('create-staff/', views.create_staff, name='create_staff'),
    path('force-password-change/', views.force_password_change, name='force_password_change'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
