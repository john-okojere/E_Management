from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import StaffProfile
from users.models import CustomUser
from .forms import AssignRoleSectionForm, EditStaffForm
from .decorator import level_required



@login_required
@level_required(4)
def manage_staff(request):
    if not request.user.is_superuser:
        return redirect('staff_dashboard')
    
    staff_profiles = CustomUser.objects.all()
    return render(request, 'shared/manage_staff.html', {'staff_profiles': staff_profiles})

@login_required
def staff_dashboard(request):
    # All available sections
    all_sections = [
        {"title": "Restaurant", "description": "Manage restaurant operations.", "url_name": "login"},
        {"title": "Arcade", "description": "Manage arcade activities.", "url_name": "arcade_cashier"},
        {"title": "Cosmetic Store", "description": "Oversee the cosmetic store.", "url_name": "login"},
        {"title": "Saloon", "description": "Handle saloon services.", "url_name": "login"},
        {"title": "Boutique", "description": "Monitor boutique operations.", "url_name": "login"},
        {"title": "Spa", "description": "Manage spa treatments.", "url_name": "login"},
        {"title": "Lounge", "description": "Oversee lounge activities.", "url_name": "login"},
    ]

    # Check the user's level
    user_level = int(request.user.staff_profile.level)  # Assuming `level` is stored as a string field in the user model

    if user_level in [1, 2]:
        # If level 1 or 2, filter sections based on the user's assigned section(s)
        sections = [request.user.staff_profile.section,] 
         # Assuming a many-to-many or related field for sections
    else:
        # If level 3 or 4, show all sections
        sections = all_sections

    return render(request, 'shared/staff_dashboard.html', {"sections": sections})

@login_required
@level_required(4)
def assign_role_section(request, staff_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admins can assign roles.")

    # Get the staff user and ensure StaffProfile exists
    user = get_object_or_404(CustomUser, id=staff_id)
    staff_profile, created = StaffProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = AssignRoleSectionForm(request.POST, instance=staff_profile)
        if form.is_valid():
            form.save()
            return redirect('manage_staff')
    else:
        form = AssignRoleSectionForm(instance=staff_profile)
    
    return render(request, 'shared/assign_role_section.html', {'form': form, 'staff': staff_profile})


@login_required
@level_required(4)
def edit_staff(request, staff_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admins can edit staff.")
    
    staff = get_object_or_404(CustomUser, id=staff_id)
    if request.method == 'POST':
        form = EditStaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('manage_staff')
    else:
        form = EditStaffForm(instance=staff)
    return render(request, 'shared/edit_staff.html', {'form': form, 'staff': staff})


@login_required
@level_required(4)
def delete_staff(request, staff_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admins can delete staff.")
    
    staff = get_object_or_404(CustomUser, id=staff_id)
    staff.delete()
    return redirect('manage_staff')
