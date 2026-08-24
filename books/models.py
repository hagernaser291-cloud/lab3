from django.db import models

from .validators import validate_book_title


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[validate_book_title],
    )
    author = models.CharField(max_length=100, default="مجهول")
    pages_count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, default="عام")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    saved_by = models.ManyToManyField(
        "account.UserAccount",
        blank=True,
        related_name="saved_books",
    )

    def __str__(self):
        return self.title