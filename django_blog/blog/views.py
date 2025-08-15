from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView


def home_view(request):
    return render(request, 'registration/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')
        
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
    
@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile')

    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'registration/profile_edit.html', {'form': form})

def login_user(request):
    return LoginView.as_view(template_name='registration/login.html')(request)

def logout_user(request):
    logout(request)
    return redirect('blog:home')