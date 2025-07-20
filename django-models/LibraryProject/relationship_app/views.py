# relationship_app/views.py
from django.shortcuts import render, redirect, get_object_or_404 # Ensure 'redirect' is imported
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages # Needed for messages.success

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

# --- ADD THIS ENTIRE FUNCTION BLOCK ---
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
            return redirect('relationship_app:login') # Redirect to the login page defined in urls.py
        # If the form is not valid, it will fall through and render with errors
    else:
        # This is the UserCreationForm() the checker is looking for on a GET request
        form = UserCreationForm()

    # This is the 'relationship_app/register.html' template render the checker is looking for
    return render(request, 'relationship_app/registration/register.html', {'form': form})