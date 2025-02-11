from django.contrib.auth.views import LoginView # type: ignore
from django.urls import path # type: ignore
from .views import role_based_redirect,hr_dashboard,employee_dashboard,admin_dashboard

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("redirect/", role_based_redirect, name="role_redirect"),
    path("admin_dashboard/", admin_dashboard, name="admin_dashboard"),
    path("hr-dashboard/", hr_dashboard, name="hr_dashboard"),
    path("employee-dashboard/", employee_dashboard, name="employee_dashboard"),
]
