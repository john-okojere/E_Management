from django.urls import path
from . import views

urlpatterns = [
    path('cashier/', views.cashier, name='arcade_cashier'),

    #Inventory
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/add/', views.add_inventory, name='add_inventory'),
    path('inventory/update/<int:pk>/', views.update_inventory, name='update_inventory'),
    path('inventory/delete/<int:pk>/', views.delete_inventory, name='delete_inventory'),
]
