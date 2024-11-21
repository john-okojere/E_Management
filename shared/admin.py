from django.contrib import admin
from .models import StaffProfile

@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'section', 'date_added')
    search_fields = ('user__worker_id', 'user__first_name', 'user__last_name', 'role', 'section')
    list_filter = ('role', 'section')
