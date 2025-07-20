from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile
from django.contrib import messages

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

def check_admin(user):
    # Check if user is authenticated and has admin role
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def check_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def check_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(check_admin)
def admin_view(request):
    # Add any admin-specific context data here
    context = {
        'admin_content': 'This is exclusive content for Admin users only.',
    }
    return render(request, 'admin_view.html', context)

@login_required
@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(check_member)
def member_view(request):
    return render(request, 'member_view.html')