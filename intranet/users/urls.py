from django.contrib.auth.views import LoginView # type: ignore
from django.urls import path # type: ignore
from .views import role_based_redirect,hr_dashboard,employee_dashboard,admin_dashboard,user_management,create_user,update_user,delete_user,announcement_management,create_announcement,update_announcement,delete_announcement,upload_user_document, view_user_info,edit_user_role,hr_announcements,create_announcement_of_hr,delete_announcement_of_hr

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("redirect/", role_based_redirect, name="role_redirect"),
    path("admin_dashboard/", admin_dashboard, name="admin_dashboard"),

    path('user-management/', user_management, name='user_management'),
    path('user-management/create/',create_user, name='create_user'),
    path('user-management/update/<int:user_id>/',update_user, name='update_user'),
    path('user-management/delete/<int:user_id>/',delete_user, name='delete_user'),

    path('announcement-management/',announcement_management, name='announcement_management'),
    path('announcement-management/create/',create_announcement, name='create_announcement'),
    path('announcement-management/update/<int:announcement_id>/',update_announcement, name='update_announcement'),
    path('announcement-management/delete/<int:announcement_id>/',delete_announcement, name='delete_announcement'),

    path("hr-dashboard/", hr_dashboard, name="hr_dashboard"),
    path('hr-dashboard/upload-document/<int:user_id>/',upload_user_document, name='upload_user_document'),
    path('hr-dashboard/user-info/<int:user_id>/', view_user_info, name='view_user_info'),
    path('hr-dashboard/edit-role/<int:user_id>/', edit_user_role, name='edit_user_role'),
    path('hr-dashboard/announcements/', hr_announcements, name='hr_announcements'),
    path('hr-dashboard/announcements/create/', create_announcement_of_hr, name='create_announcement_of_hr'),
    path('hr-dashboard/announcements/delete/<int:announcement_id>/', delete_announcement_of_hr, name='delete_announcement_of_hr'),

    path("employee-dashboard/", employee_dashboard, name="employee_dashboard"),
]
