from django.http import HttpResponseForbidden

def user_passes_test(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You must be logged in.")
        return view_func(request, *args, **kwargs)
    return wrapper
