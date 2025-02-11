from django.shortcuts import redirect,render,get_object_or_404 # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.http import HttpResponseForbidden, HttpResponse # type: ignore
from users.models import CustomUser
from django.contrib import messages # type: ignore
from django.urls import reverse # type: ignore


# Checking user role and redirect to appropriate dashboard
@login_required
def role_based_redirect(request):
    
    user = request.user
    if user.role == 'Admin':  # Admin
        return redirect("admin_dashboard")
    elif user.role == 'HR':  # HR Role
        return redirect("hr_dashboard")
    elif user.role in ['IT', 'Marketing']:  # Employee Roles
        return redirect("employee_dashboard")
    else:
        return HttpResponseForbidden("You do not have access.")

# Admin Dashboard is Added    
@login_required
def admin_dashboard(request):
     # Ensure only Admin users can access this view
    if request.user.role != "Admin":
        return render(request, "403.html", status=403)  # Custom 403 page if user isn't Admin
    
    total_users = CustomUser.objects.filter(is_active=True).count()
    
    # Render the dashboard
    return render(request, "admin_dashboard.html", {"total_users": total_users})

# HR Dashboard is Added 
@login_required
def hr_dashboard(request):
    return HttpResponse("Welcome to the HR Dashboard!")

# Employee Dashboard is Added 
@login_required
def employee_dashboard(request):
    return HttpResponse("Welcome to the Employee Dashboard!")