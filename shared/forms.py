from django import forms
from .models import StaffProfile
from users.models import CustomUser

class AssignRoleSectionForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['role', 'section', 'level']

class EditStaffForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']
