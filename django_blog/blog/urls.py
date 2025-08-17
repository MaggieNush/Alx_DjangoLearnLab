from . import views
from django.urls import path, include
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('post/new/', PostCreateView.as_view(), name='post_create'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('', views.home_view, name='home'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/edit/', views.profile_edit, name='edit_profile'),

    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

]