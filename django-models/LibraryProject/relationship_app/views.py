# relationship_app/views.py
from django.shortcuts import render, redirect, get_object_or_404 # ADD 'redirect' here
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages # ADD this import for 'messages'

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
    A class-based view (using Django's DetailView) to display the details
    of a specific library, including all books it contains.
    This view is designed to be accessed via a primary key (pk) in the URL.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_year'] = 2025
        return context

# --- Function-based View for User Registration ---
def register(request):
    """
    Handles user registration.
    This view processes the UserCreationForm for new user sign-ups.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('relationship_app:login')
        # If the form is not valid, it will fall through and render with errors
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/registration/register.html', {'form': form})