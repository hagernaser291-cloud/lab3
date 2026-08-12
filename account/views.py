from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# 1. دالة إنشاء حساب جديد ويضاف مباشرة لقاعدة البيانات
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # حفظ المستخدم تلقائياً في قاعدة البيانات
            login(request, user)  # تسجيل دخوله مباشرة بعد التسجيل
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

# 2. دالة تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

# 3. دالة تسجيل الخروج
def logout_view(request):
    logout(request)
    return redirect('home')