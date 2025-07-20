# relationship_app/views/admin_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

def check_admin(user):
    """Check if user has Admin role"""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(check_admin, login_url='/accounts/login/')  # Redirect to login if not authenticated
def admin_view(request):
    """View accessible only to Admin users"""
    if not check_admin(request.user):
        raise PermissionDenied  # Show 403 error if role check fails
    
    context = {
        'message': 'Welcome, Admin!',
        'features': [
            'Manage all users',
            'Configure system settings',
            'Access admin reports'
        ]
    }
    return render(request, 'admin_dashboard.html', context)