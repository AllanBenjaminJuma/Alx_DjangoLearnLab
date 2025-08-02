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
from django.contrib.auth.decorators import permission_required

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
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("You do not have a profile associated with this page.")
    
    if profile.role != 'member':
        return HttpResponseForbidden("You are not allowed to view this page.")
    
    return render(request, 'relationship_app/member_view.html')
        
from .forms import BookForm

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

from django.shortcuts import get_object_or_404

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect('list_books')
    return render(request, 'relationship_app/confirm_delete.html', {'book': book})
