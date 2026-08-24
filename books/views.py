from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from account.models import UserAccount

from .forms import BookForm
from .models import Book


def home(request):
    query = request.GET.get("q", "").strip()
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    books = (
        books.exclude(title__isnull=True)
        .annotate(saved_count=Count("saved_by", distinct=True))
        .order_by("-created_at", "title")
    )

    total_books = Book.objects.count()
    has_books = Book.objects.exists()
    average_price = Book.objects.aggregate(average=Avg("price"))["average"]
    categories = list(
        Book.objects.values_list("category", flat=True)
        .distinct()
        .order_by("category")
    )

    context = {
        "query": query,
        "app_title": "مكتبتي الرقمية - Software Engineering Lab",
        "welcome_msg": "WELCOME to Books Library Application!",
        "page_description": "تطبيق لإدارة ورصد الكتب والمراجع المتاحة",
        "current_date": timezone.now(),
        "books": books,
        "empty_list": [] if has_books else ["لا توجد كتب بعد"],
        "total_books": total_books,
        "average_price": average_price,
        "categories": categories,
    }
    return render(request, "books/home.html", context)


def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        book = None

    is_saved = bool(
        book
        and request.user.is_authenticated
        and book.saved_by.filter(pk=request.user.pk).exists()
    )

    return render(
        request,
        "books/detail.html",
        {
            "book": book,
            "book_id": book_id,
            "is_saved": is_saved,
        },
    )


@login_required
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("books:detail", book_id=book.pk)
    else:
        form = BookForm()

    return render(
        request,
        "books/book_form.html",
        {"form": form, "page_title": "إضافة كتاب"},
    )


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:detail", book_id=book.pk)
    else:
        form = BookForm(instance=book)

    return render(
        request,
        "books/book_form.html",
        {
            "form": form,
            "book": book,
            "page_title": "تعديل بيانات الكتاب",
        },
    )


@login_required
def toggle_saved(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user_account = UserAccount.objects.filter(user=request.user).first()

    if user_account is None:
        return redirect("account:register")

    if book.saved_by.filter(pk=user_account.pk).exists():
        book.saved_by.remove(user_account)
    else:
        book.saved_by.add(user_account)

    return redirect("books:detail", book_id=book.pk)