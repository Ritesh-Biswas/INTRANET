from django.contrib.auth.models import AbstractUser # type: ignore
from django.db import models # type: ignore

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('HR', 'HR'),
        ('IT', 'IT'),
        ('Marketing', 'Marketing'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='IT')
    is_active = models.BooleanField(default=True)  # For soft delete functionality

    def is_editable_by_hr(self):
        """Check if the user is editable by an HR user."""
        return self.role in ['IT', 'Marketing']  # Editable roles for HR

class Announcement(models.Model):
    ANNOUNCEMENT_TYPE_CHOICES = [
        ('All Users', 'All Users'),
        ('HR', 'HR'),
        ('IT', 'IT'),
        ('Marketing', 'Marketing'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    attachment = models.FileField(upload_to='announcements/', blank=True, null=True)  # Optional attachment
    announcement_type = models.CharField(max_length=20, choices=ANNOUNCEMENT_TYPE_CHOICES, default='All Users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

#Model for User Document
class UserDocument(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='user_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.user.username} - {self.document.name}"
