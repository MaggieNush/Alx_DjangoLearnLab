from django.urls import path
from . import views # Import views from the current app

app_name = 'relationship_app' 

urlpatterns = [
    # URL for the function-based view to list all books
    path('books/', views.all_books_list_view, name='books_list'),

    # URL for the class-based view to show individual library details
    # <int:pk> captures the primary key from the URL and passes it to the view
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]