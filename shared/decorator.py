from django.http import HttpResponseForbidden
from functools import wraps

def level_required(min_level):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, "staff_profile"):
                staff_profile = request.user.staff_profile
                if int(staff_profile.level) >= min_level or staff_profile.user.is_staff:
                    return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have the required access level.")
        return _wrapped_view
    return decorator

def role_or_section_required(required_role=None, required_section=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, "staff_profile"):
                staff_profile = request.user.staff_profile
                if (required_role and staff_profile.role == required_role) or \
                   (required_section and staff_profile.section == required_section):
                    return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("Access restricted based on role or section.")
        return _wrapped_view
    return decorator
