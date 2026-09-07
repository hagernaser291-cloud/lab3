from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Notification

def register_view(request):
    if request.user.is_authenticated:
        return redirect("books:home")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("books:home")
    else:
        form = RegistrationForm()
    return render(request, "account/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("books:home")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("books:home")
    else:
        form = AuthenticationForm(request)
    return render(request, "account/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("books:home")

@login_required(login_url="account:login")
def notifications_view(request):
    notifications = Notification.objects.filter(
        recipient=request.user,
    ).order_by("-created_at")

    return render(
        request,
        "account/notifications.html",
        {"notifications": notifications},
    )