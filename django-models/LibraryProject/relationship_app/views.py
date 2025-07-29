from django.shortcuts import render
from .models import Book
from .models import Library

from django.views.generic.detail import DetailView

from django.contrib import messages
from django.shortcuts import render, redirect

from django.views.generic import CreateView
from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

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


