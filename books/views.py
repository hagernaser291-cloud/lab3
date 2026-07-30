from django.shortcuts import render
from datetime import datetime

def home(request):
    # 1. متغيرات محلية (Local Variables)
    app_title = "مكتبتي الرقمية - Software Engineering Lab"
    welcome_msg = "  WELCOME to Books Library Application!  "  # للـ filters
    page_description = "تطبيق لإدارة ورصد الكتب والمراجع المتاحة"
    current_date = datetime.now()
    empty_list = []  # لاختبار شرط القائمة الفارغة DTL

    # قائمة من القواميس تمثل بيانات الكتب
    books_list = [
        {"id": 1, "title": "clean code", "author": "Robert Martin", "price": 45.5, "pages": 464, "category": "software engineering", "is_available": True},
        {"id": 2, "title": "PYTHON CRASH COURSE", "author": "Eric Matthes", "price": 30.0, "pages": 544, "category": "programming", "is_available": True},
        {"id": 3, "title": "design patterns", "author": "Erich Gamma", "price": 55.0, "pages": 395, "category": "software architecture", "is_available": False},
        {"id": 4, "title": "THE PRAGMATIC PROGRAMMER", "author": "Andrew Hunt", "price": 50.0, "pages": 352, "category": "software engineering", "is_available": True},
    ]

    # سياق البيانات المرسل للملف العرض
    context = {
        "app_title": app_title,
        "welcome_msg": welcome_msg,
        "page_description": page_description,
        "current_date": current_date,
        "books": books_list,
        "empty_list": empty_list,
    }
    
    return render(request, "books/home.html", context)

def detail(request, book_id):
    # دالة تفاصيل كتاب معين
    books_list = [
        {"id": 1, "title": "Clean Code", "author": "Robert Martin", "price": 45.5, "pages": 464, "category": "Software Engineering"},
        {"id": 2, "title": "Python Crash Course", "author": "Eric Matthes", "price": 30.0, "pages": 544, "category": "Programming"},
    ]
    # البحث عن الكتاب بالـ ID
    selected_book = next((b for b in books_list if b["id"] == book_id), None)
    
    return render(request, "books/detail.html", {"book": selected_book, "book_id": book_id})