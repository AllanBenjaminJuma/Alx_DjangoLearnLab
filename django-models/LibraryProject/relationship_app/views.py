from django.shortcuts import render
from .models import Book
from .models import Library
from .models import UserProfile

from django.views.generic.detail import DetailView

from .decorators import user_passes_test

from django.contrib import messages
from django.shortcuts import render, redirect

from django.views.generic import CreateView
from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseForbidden

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm() # built-in form for user registration
    return render(request, 'relationship_app/register.html', {'form': form})

@login_required
@user_passes_test
def admin_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("You do not have a profile associated with your account")
    
    if profile.role != 'Admin':
        return HttpResponseForbidden("You are not allowed to view this page.")
    
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test
def librarian_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("You do not have a profile associated with your account.")
    
    if profile.role != 'Librarian':
        return HttpResponseForbidden("You are not allowed to view this page.")
    
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test
def member_view(request):
    try:
        profile = request.userprofile
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("You do not have a profile associated with this page.")
    
    if profile.role != 'member':
        return HttpResponseForbidden("You are not allowed to view this page.")
    
    return render(request, 'relationship_app/member_view.html')
        
