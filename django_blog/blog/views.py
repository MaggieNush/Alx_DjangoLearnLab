from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'User does not exist.')
            return render(request, 'login.html')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password.')
            return redirect('home')
        
        return render(request, 'login.html')
    
def logout_page(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')
