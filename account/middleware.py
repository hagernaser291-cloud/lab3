from django.shortcuts import redirect


class AuthenticatedAccountPagesMiddleware:
    """
    يمنع المستخدم المسجل من فتح صفحات الدخول والتسجيل.
    المستخدم المجهول يستطيع الوصول إليهما بشكل طبيعي.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_paths = {
            "/account/login",
            "/account/register",
        }
        current_path = request.path_info.rstrip("/")

        if request.user.is_authenticated and current_path in restricted_paths:
            return redirect("books:home")

        return self.get_response(request)