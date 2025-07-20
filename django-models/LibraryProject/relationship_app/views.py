from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Book, Library

# --- Function-based View: List All Books ---
def all_books_list_view(request):
    """
    A function-based view to display a comprehensive list of all books
    available in the library system, along with their authors.
    """
    all_books = Book.objects.all().select_related('author').order_by('title')

    context = {
        'books': all_books,
        'page_title': 'Our Complete Book Collection',
        'intro_message': 'Explore every title we have at a glance.'
    }

    return render(request, 'relationship_app/list_books.html', context)


# --- Class-based View: Library Details ---
class LibraryDetailView(DetailView):
    """
    Displays details of a specific library including all books it contains.
    Accessed via primary key (pk).
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_year'] = 2025  # Example of adding extra context
        return context


# --- User Registration View ---
def register_view(request):
    """
    Handles new user registration using Django's built-in UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the new user
            return redirect('home')  # Change 'home' to the name of your home route
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})
