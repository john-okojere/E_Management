from django.db import models
from django.contrib.auth.models import AbstractUser
from shared.models import StaffProfile
from decimal import Decimal
from django.utils.timezone import now

class Inventory(models.Model):
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.quantity} items"

    def is_in_stock(self):
        return self.quantity > 0

class Sale(models.Model):
    cashier = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)  # Who handled the sale
    total = models.DecimalField(max_digits=15, decimal_places=2)  # Total amount for the sale
    date = models.DateTimeField(auto_now_add=True)  # When the sale occurred

    def __str__(self):
        return f"Sale #{self.id} by {self.cashier}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")  # Reference to the sale
    product = models.ForeignKey(Inventory, on_delete=models.CASCADE)  # The product being sold
    quantity = models.PositiveIntegerField()  # Quantity sold
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per unit
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total price for this line item (price * quantity)

    def __str__(self):
        return f"{self.product.name} x{self.quantity} in Sale #{self.sale.id}"


class Receipt(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Discount(models.Model):
    cashier = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    proposed_discount = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(StaffProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='approver')
