from django.contrib.auth.decorators import user_passes_test

def user_passes_test(role):
    def decorator(view_func):
        def check_role(user):
            return user.is_authenticated and hasattr(user, 'user profile') and user.userprofile.role == role
        return user_passes_test(check_role)(view_func)
    return