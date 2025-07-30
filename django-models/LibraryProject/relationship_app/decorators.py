from django.contrib.auth.decorators import user_passes_test

def role_required(role):
    def decorator(view_func):
        def check_role(user):
            return user_is_authenticated and hasattr(user, 'user profile') and user.userprofile.role == role
        return user_passes_test(check_role)(view_func)
    return decorator