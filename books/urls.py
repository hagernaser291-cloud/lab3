from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.create_book, name="create"),
    path("<int:book_id>/", views.detail, name="detail"),
    path("<int:book_id>/edit/", views.edit_book, name="edit"),
    path("<int:book_id>/save/", views.toggle_saved, name="toggle_saved"),
]