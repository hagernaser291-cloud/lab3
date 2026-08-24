from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import UserAccount


User = get_user_model()


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, label="الاسم الكامل")
    email = forms.EmailField(label="البريد الإلكتروني")
    phone = forms.CharField(max_length=15, required=False, label="رقم الهاتف")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "full_name", "email", "phone")

    def clean_email(self):
        email = self.cleaned_data["email"].lower().strip()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("هذا البريد الإلكتروني مستخدم من قبل.")
        if UserAccount.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("هذا البريد الإلكتروني مرتبط بحساب موجود.")
        return email

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserAccount.objects.update_or_create(
                user=user,
                defaults={
                    "username": user.username,
                    "full_name": self.cleaned_data["full_name"].strip(),
                    "email": self.cleaned_data["email"],
                    "phone": self.cleaned_data.get("phone", "").strip() or None,
                },
            )
        return user