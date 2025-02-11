from django.contrib import admin # type: ignore
from .models import Announcement,UserDocument

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'announcement_type', 'created_at')
    search_fields = ('title', 'announcement_type')

@admin.register(UserDocument)
class UserDocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'document', 'uploaded_at')    