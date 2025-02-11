from django.contrib.auth.views import LoginView # type: ignore
from django.urls import path # type: ignore
from .views import role_based_redirect,hr_dashboard,employee_dashboard,admin_dashboard,user_management,create_user,update_user,delete_user

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("redirect/", role_based_redirect, name="role_redirect"),
    path("admin_dashboard/", admin_dashboard, name="admin_dashboard"),
    path('user-management/', user_management, name='user_management'),
    path('user-management/create/',create_user, name='create_user'),
    path('user-management/update/<int:user_id>/',update_user, name='update_user'),
    path('user-management/delete/<int:user_id>/',delete_user, name='delete_user'),
    path("hr-dashboard/", hr_dashboard, name="hr_dashboard"),
    path("employee-dashboard/", employee_dashboard, name="employee_dashboard"),
]
