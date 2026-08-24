from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import RegistrationForm


def register_view(request):
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