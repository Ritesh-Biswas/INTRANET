from django.shortcuts import redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.http import HttpResponseForbidden, HttpResponse # type: ignore

@login_required
def role_based_redirect(request):
    # Check user role and redirect to appropriate dashboard
    user = request.user
    if user.role == 'Admin':  # Admin
        return redirect("admin_dashboard")
    elif user.role == 'HR':  # HR Role
        return redirect("hr_dashboard")
    elif user.role in ['IT', 'Marketing']:  # Employee Roles
        return redirect("employee_dashboard")
    else:
        return HttpResponseForbidden("You do not have access.")
    
@login_required
def admin_dashboard(request):
    return HttpResponse("Welcome to the Admin Dashboard!")

@login_required
def hr_dashboard(request):
    return HttpResponse("Welcome to the HR Dashboard!")

@login_required
def employee_dashboard(request):
    return HttpResponse("Welcome to the Employee Dashboard!")