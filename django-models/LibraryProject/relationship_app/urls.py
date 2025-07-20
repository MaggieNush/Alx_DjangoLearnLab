from django.urls import path
from . import views # Import all views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'relationship_app' 

urlpatterns = [
    path('books/', views.all_books_list_view, name='books_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/registration/logged_out.html'), name='logout'),
    path('admin-portal/', views.admin_view, name='admin_portal'),
    # path('librarian/', librarian_view, name='librarian_view'),
    
    # path('member/', member_view, name='member_view'),

    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

]