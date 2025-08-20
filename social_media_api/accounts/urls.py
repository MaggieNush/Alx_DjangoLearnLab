from django.urls import path
from .views import FollowToggleView, RegistrationView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowToggleView.as_view(), name='follow_toggle'),

]