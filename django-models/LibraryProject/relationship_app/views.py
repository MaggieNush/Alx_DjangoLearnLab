# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView # Correctly using DetailView for a specific item
from .models import Book, Library # Import your models

# --- Function-based View: List All Books ---
def all_books_list_view(request):
    """
    A function-based view to display a comprehensive list of all books
    available in the library system, along with their authors.
    """
    # Fetch all Book objects from the database.
    # .select_related('author') is an optimization to fetch author data
    # in the same database query, preventing N+1 query problems.
    all_books = Book.objects.all().select_related('author').order_by('title')

    # Prepare the context dictionary to pass data to the template.
    context = {
        'books': all_books,
        'page_title': 'Our Complete Book Collection',
        'intro_message': 'Explore every title we have at a glance.'
    }
    # Render the list_books.html template with the prepared context.
    return render(request, 'relationship_app/list_books.html', context)


# --- Class-based View: Library Details ---
class LibraryDetailView(DetailView):
    """
    A class-based view (using Django's DetailView) to display the details
    of a specific library, including all books it contains.
    This view is designed to be accessed via a primary key (pk) in the URL.
    """
    model = Library # Specify the model this view will operate on.
    template_name = 'relationship_app/library_detail.html' # Path to your template.
    context_object_name = 'library' # The variable name to use for the Library object in the template.

    # You can customize the queryset if needed, but for a simple detail, model = Library is enough.
    # def get_queryset(self):
    #     # Example: If you wanted to prefetch books for every library detail view
    #     return Library.objects.all().prefetch_related('books__author')

    # get_context_data is optional, used if you need to add extra context beyond the single object.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any extra context specific to a library's details page
        context['current_year'] = 2025 # Just an example of extra context
        return context# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView # Correctly using DetailView for a specific item
from .models import Book, Library # Import your models

# --- Function-based View: List All Books ---
def all_books_list_view(request):
    """
    A function-based view to display a comprehensive list of all books
    available in the library system, along with their authors.
    """
    # Fetch all Book objects from the database.
    # .select_related('author') is an optimization to fetch author data
    # in the same database query, preventing N+1 query problems.
    all_books = Book.objects.all().select_related('author').order_by('title')

    # Prepare the context dictionary to pass data to the template.
    context = {
        'books': all_books,
        'page_title': 'Our Complete Book Collection',
        'intro_message': 'Explore every title we have at a glance.'
    }
    # Render the list_books.html template with the prepared context.
    return render(request, 'relationship_app/list_books.html', context)


# --- Class-based View: Library Details ---
class LibraryDetailView(DetailView):
    """
    A class-based view (using Django's DetailView) to display the details
    of a specific library, including all books it contains.
    This view is designed to be accessed via a primary key (pk) in the URL.
    """
    model = Library # Specify the model this view will operate on.
    template_name = 'relationship_app/library_detail.html' # Path to your template.
    context_object_name = 'library' # The variable name to use for the Library object in the template.

    # You can customize the queryset if needed, but for a simple detail, model = Library is enough.
    # def get_queryset(self):
    #     # Example: If you wanted to prefetch books for every library detail view
    #     return Library.objects.all().prefetch_related('books__author')

    # get_context_data is optional, used if you need to add extra context beyond the single object.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any extra context specific to a library's details page
        context['current_year'] = 2025 # Just an example of extra context
        return context