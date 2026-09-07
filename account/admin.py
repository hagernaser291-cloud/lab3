from django.contrib import admin

from .models import Notification, UserAccount

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "full_name",
        "email",
        "phone",
        "user",
        "created_at",
    )
    search_fields = ("username", "full_name", "email", "phone")
    list_filter = ("created_at",)
    ordering = ("-created_at", "username")

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("recipient", "title", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("recipient__username", "title", "message")
    ordering = ("-created_at",)