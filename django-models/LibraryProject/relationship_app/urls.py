from django.urls import path
from . import views # Import views
from django.contrib.auth.views import LoginView, LogoutView
from .admin_view import admin_view

app_name = 'relationship_app' 

urlpatterns = [
    # URL for the function-based view to list all books
    path('books/', views.all_books_list_view, name='books_list'),

    # URL for the class-based view to show individual library details
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    path('books/', views.all_books_list_view, name='books_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # --- NEW: Authentication URLs ---

    # URL for user registration (will be a custom function-based view)
    # path('register/', views.register, name='register'),

    # URL for user login (using Django's built-in LoginView)
    # We specify a template_name for the login form.
    path('login/', LoginView.as_view(template_name='relationship_app/registration/login.html'), name='login'),

    # URL for user logout (using Django's built-in LogoutView)
    # We specify a template_name for the logged-out confirmation page.
    path('logout/', LogoutView.as_view(template_name='relationship_app/registration/logged_out.html'), name='logout'),

    path('admin-portal/', admin_view, name='admin_portal'),
    # path('librarian/', librarian_view, name='librarian_view'),
    
    # path('member/', member_view, name='member_view'),

]