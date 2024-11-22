from django.contrib import admin
from .models import Inventory, Sale, SaleItem, Receipt, SaleDiscount, SaleItemDiscount

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'staff', 'date', 'is_in_stock')
    list_filter = ('date', 'staff')
    search_fields = ('name', 'description', 'staff__user__worker_id')
    ordering = ('-date',)

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1
    fields = ('product', 'quantity', 'price', 'total')
    readonly_fields = ('total',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'cashier', 'total', 'date')
    list_filter = ('date', 'cashier__user__worker_id')
    search_fields = ('cashier__user__worker_id', 'id')
    ordering = ('-date',)
    inlines = [SaleItemInline]

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale', 'product', 'quantity', 'price', 'total')
    list_filter = ('sale__date', 'product__name')
    search_fields = ('sale__id', 'product__name')
    ordering = ('-sale__date',)

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_number', 'sale', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('receipt_number', 'sale__id')
    ordering = ('-created_at',)

@admin.register(SaleDiscount)
class SaleDiscountAdmin(admin.ModelAdmin):
    list_display = ('sale', 'cashier', 'proposed_discount', 'approved', 'approved_by')
    list_filter = ('approved', 'cashier__user__worker_id', 'sale__date')
    search_fields = ('sale__id', 'cashier__user__worker_id')
    ordering = ('-sale__date',)

@admin.register(SaleItemDiscount)
class SaleItemDiscountAdmin(admin.ModelAdmin):
    list_display = ('sale', 'cashier', 'proposed_discount', 'approved', 'approved_by')
    list_filter = ('approved', 'cashier__user__worker_id', 'sale__sale__date')
    search_fields = ('sale__sale__id', 'cashier__user__worker_id')
    ordering = ('-sale__sale__date',)
