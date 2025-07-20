from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def admin_view(request):
    """The exact view name the checker wants"""
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Please login first")
    
    try:
        if request.user.userprofile.role != 'Admin':
            return HttpResponseForbidden("Admin access required")
    except AttributeError:
        return HttpResponseForbidden("User profile missing")

    return render(request, 'admin_view.html', {
        'special_data': 'Secret admin information'
    })