from django.contrib import admin

from .models import UserAccount


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