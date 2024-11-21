
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from .forms import CreateStaffForm, PasswordChangeFormWithPrompt
from .models import CustomUser
from django.contrib import messages
from django.http import HttpResponseForbidden
from shared.decorator import level_required

@login_required
@level_required(4)
def create_staff(request):
    if not request.user.is_superuser:
        return redirect('staff_dashboard')
    if request.method == "POST":
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_staff')
    else:
        form = CreateStaffForm()
    return render(request, 'shared/create_staff.html', {'form': form})


@login_required
def force_password_change(request):
    if request.method == 'POST':
        form = PasswordChangeFormWithPrompt(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)  # Keep the user logged in
            return redirect('manage_staff')
    else:
        form = PasswordChangeFormWithPrompt(user=request.user)
    return render(request, 'shared/force_password_change.html', {'form': form})


def login_view(request):
    """
    Handles user login.
    """
    if request.method == 'POST':
        worker_id = request.POST.get('worker_id')  # Expecting 'worker_id' as the login username
        password = request.POST.get('password')
        user = authenticate(request, username=worker_id, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff:  # Redirect staff to the staff dashboard
                return redirect('manage_staff')
            else:
                return redirect('staff_dashboard')  # Redirect customers to their dashboard
        else:
            messages.error(request, "Invalid Worker ID or Password")
            return redirect('login')
    
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """
    Handles user logout.
    """
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')