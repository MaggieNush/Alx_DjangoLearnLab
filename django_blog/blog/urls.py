from . import views
from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('', views.home_view, name='home'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/edit/', views.profile_edit, name='edit_profile'),
]