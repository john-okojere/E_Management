from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import CustomUser

class CreateStaffForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'value': '123456'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password('123456')  # Default password
        if commit:
            user.save()
        return user


class PasswordChangeFormWithPrompt(PasswordChangeForm):
    """
    Forces the user to change their password on first login.
    """
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_first_login = False  # Mark as no longer the first login
        if commit:
            user.save()
        return user

