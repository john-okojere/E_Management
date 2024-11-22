from django.urls import path
from . import views

urlpatterns = [
    path('cashier/', views.cashier, name='arcade_cashier'),

    #Inventory
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/add/', views.add_inventory, name='add_inventory'),
    path('inventory/update/<int:pk>/', views.update_inventory, name='update_inventory'),
    path('inventory/delete/<int:pk>/', views.delete_inventory, name='delete_inventory'),

    #sales
    path('create-sale/', views.create_sale, name='create_sale'),
    path('add-sale-item/', views.add_sale_item, name='add_sale_item'),
    path('complete-sale/', views.complete_sale, name='complete_sale'),
    
    #discount
    path('create-sale-discount/', views.apply_sale_discount, name='apply_sale_discount'),
    path('apply-sale-item-discount/', views.apply_sale_item_discount, name='apply_sale_item_discount'),

]
