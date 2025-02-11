from django.contrib import admin # type: ignore
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'announcement_type', 'created_at')
    search_fields = ('title', 'announcement_type')