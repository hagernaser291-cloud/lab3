from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "price",
        "is_available",
        "saved_books_count",
        "created_at",
    )
    search_fields = ("title", "author", "category")
    list_filter = ("is_available", "category", "created_at")
    ordering = ("-created_at", "title")

    @admin.display(description="عدد الحفظ")
    def saved_books_count(self, obj):
        return obj.saved_by.count()