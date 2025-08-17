from . import views
from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('new/', PostCreateView.as_view(), name='post_create'),
    path('', views.home_view, name='home'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/edit/', views.profile_edit, name='edit_profile'),
]