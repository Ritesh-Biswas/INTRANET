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
