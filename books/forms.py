from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "pages_count",
            "price",
            "category",
            "is_available",
            "description",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_title(self):
        return " ".join(self.cleaned_data["title"].split())