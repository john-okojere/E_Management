from django.db import models
from users.models import CustomUser  # Assuming the CustomUser model is in the users app.


LEVELS = (
    ('1', 'Level 1 - Limited Access: Can only view assigned section (e.g., Cashier).'),
    ('2', 'Level 2 - Restricted Access: Can read and modify content within assigned sections (e.g., Manager).'),
    ('3', 'Level 3 - Read-Only Access: Can view details but cannot edit (e.g., Accountant).'),
    ('4', 'Level 4 - Full Access: Can read and modify content across all sections (e.g., IT Manager, General Manager, CEO).'),
)


class StaffProfile(models.Model):
    """
    A model to represent additional information about staff.
    """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="staff_profile"
    )
    role = models.CharField(
        max_length=50,
        choices=[
            ("cashier", "Cashier"),
            ("manager", "Manager"),
            ("waiter", "Waiter"),
            ("it_manager", "IT Manager"),
            ("general_manager", "General Manager"),
            ("accountant", "Accountant"),
            ("ceo", "CEO"),
        ],
        blank=True,
        null=True,
    )
    section = models.CharField(
        max_length=50,
        choices=[
            ("restaurant", "Restaurant"),
            ("arcade", "Arcade"),
            ("cosmetic_store", "Cosmetic Store"),
            ("saloon", "Saloon"),
            ("boutique", "Boutique"),
            ("spa", "Spa"),
            ("lounge", "Lounge"),
            ("all", "All"),
        ],
        blank=True,
        null=True,
    )
    level = models.CharField(max_length=5, choices= LEVELS, default='1')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.worker_id} - {self.role or 'No Role Assigned'} ({self.section or 'No Section Assigned'})"

    class Meta:
        verbose_name = "Staff Profile"
        verbose_name_plural = "Staff Profiles"
        ordering = ['user__worker_id']  # Sort by phone number by default
