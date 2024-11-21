from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('worker_id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_first_login')
    list_filter = ('is_staff', 'is_active', 'is_first_login')
    search_fields = ('worker_id', 'first_name', 'last_name', 'email')
    ordering = ('worker_id',)
    fieldsets = (
        (None, {'fields': ('worker_id', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_first_login', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('worker_id', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

# Register the custom user model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
