from django.shortcuts import redirect

class ForcePasswordChangeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_first_login:
            if request.path != '/auth/force-password-change/':  # Allow access to password change page
                return redirect('force_password_change')
        return self.get_response(request)
