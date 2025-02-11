from django.shortcuts import redirect,render,get_object_or_404 # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.http import HttpResponseForbidden, HttpResponse # type: ignore
from users.models import CustomUser,Announcement,UserDocument
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


@login_required
def user_management(request):
    # Ensure only Admin users can access this view
    if request.user.role != "Admin":
        return HttpResponseForbidden("You are not authorized to access this page.")

    # Fetch all active users
    users = CustomUser.objects.filter(is_active=True).order_by('-id')
    return render(request, "user_management.html", {"users": users})


@login_required
def create_user(request):
    if request.user.role != "Admin":
        return HttpResponseForbidden("You are not authorized to access this page.")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        role = request.POST.get("role")
        password = request.POST.get("password")

        # Create a new user
        new_user = CustomUser.objects.create_user(
            username=username,
            email=email,
            role=role,
            password=password,
        )
        messages.success(request, f"User {username} created successfully!")
        return redirect(reverse("user_management"))

    return render(request, "create_user.html")


@login_required
def update_user(request, user_id):
    if request.user.role != "Admin":
        return HttpResponseForbidden("You are not authorized to access this page.")

    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.role = request.POST.get("role")
        user.save()
        messages.success(request, f"User {user.username} updated successfully!")
        return redirect(reverse("user_management"))

    return render(request, "update_user.html", {"user": user})


@login_required
def delete_user(request, user_id):
    if request.user.role != "Admin":
        return HttpResponseForbidden("You are not authorized to access this page.")

    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = False  # Soft delete
    user.save()
    messages.success(request, f"User {user.username} deleted successfully!")
    return redirect(reverse("user_management"))

@login_required
def announcement_management(request):
    if request.user.role != "Admin":
        return HttpResponseForbidden("You are not authorized to access this page.")

    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, "announcement_management.html", {"announcements": announcements})


@login_required
def create_announcement(request):
    if request.user.role != "Admin":
        return HttpResponseForbidden("You are not authorized to access this page.")

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        announcement_type = request.POST.get("announcement_type")
        attachment = request.FILES.get("attachment")

        Announcement.objects.create(
            title=title,
            content=content,
            announcement_type=announcement_type,
            attachment=attachment,
        )
        messages.success(request, "Announcement created successfully!")
        return redirect(reverse("announcement_management"))

    return render(request, "create_announcement.html")


@login_required
def update_announcement(request, announcement_id):
    if request.user.role != "Admin":
        return HttpResponseForbidden("You are not authorized to access this page.")

    announcement = get_object_or_404(Announcement, id=announcement_id)

    if request.method == "POST":
        announcement.title = request.POST.get("title")
        announcement.content = request.POST.get("content")
        announcement.announcement_type = request.POST.get("announcement_type")
        if request.FILES.get("attachment"):
            announcement.attachment = request.FILES.get("attachment")
        announcement.save()
        messages.success(request, "Announcement updated successfully!")
        return redirect(reverse("announcement_management"))

    return render(request, "update_announcement.html", {"announcement": announcement})


@login_required
def delete_announcement(request, announcement_id):
    if request.user.role != "Admin":
        return HttpResponseForbidden("You are not authorized to access this page.")

    announcement = get_object_or_404(Announcement, id=announcement_id)
    announcement.delete()
    messages.success(request, "Announcement deleted successfully!")
    return redirect(reverse("announcement_management"))




# HR Dashboard is Added 
@login_required
def hr_dashboard(request):
    if request.user.role != "HR":
        return HttpResponseForbidden("You are not authorized to access this page.")

    users = CustomUser.objects.filter(role__in=['IT', 'Marketing']).order_by('username')
    return render(request, "hr_dashboard.html", {"users": users})

@login_required
def upload_user_document(request, user_id):
    if request.user.role != "HR":
        return HttpResponseForbidden("You are not authorized to access this page.")

    user = get_object_or_404(CustomUser, id=user_id)
    if not user.is_editable_by_hr():
        return HttpResponseForbidden("You are not authorized to upload documents for this user.")

    if request.method == "POST":
        document = request.FILES.get("document")
        if document:
            UserDocument.objects.create(user=user, document=document)
            messages.success(request, "Document uploaded successfully!")
        return redirect(reverse("hr_dashboard"))

    return render(request, "upload_user_document.html", {"user": user})

@login_required
def edit_user_role(request, user_id):
    if request.user.role != "HR":
        return HttpResponseForbidden("You are not authorized to access this page.")

    user = get_object_or_404(CustomUser, id=user_id)
    if not user.is_editable_by_hr():
        return HttpResponseForbidden("You are not authorized to edit this user's role.")

    if request.method == "POST":
        new_role = request.POST.get("role")
        if new_role and new_role in dict(CustomUser.ROLE_CHOICES).keys():
            user.role = new_role
            user.save()
            messages.success(request, "User role updated successfully!")
            return redirect(reverse("hr_dashboard"))

    return render(request, "edit_user_role.html", {"user": user})

@login_required
def view_user_info(request, user_id):
    if request.user.role != "HR":
        return HttpResponseForbidden("You are not authorized to access this page.")

    user = get_object_or_404(CustomUser, id=user_id)
    if not user.is_editable_by_hr():
        return HttpResponseForbidden("You are not authorized to view this user's info.")

    documents = UserDocument.objects.filter(user=user)
    return render(request, "view_user_info.html", {"user": user, "documents": documents})

# Employee Dashboard is Added 
@login_required
def employee_dashboard(request):
    return HttpResponse("Welcome to the Employee Dashboard!")

