from django import template

register = template.Library()

@register.filter(name='book_status')
def book_status(value):
    """
    فلتر مخصص يفحص اسم الكتاب أو حالته ويعيد نص التوفر
    """
    if not value or str(value).strip() == "":
        return "ادخل اسم الكتاب في البحث"

    # قاموس يطابق أسماء الكتب مع حالتها
    availability_map = {
        "الحساسة": "📗 متوفر حالياً في المكتبة",
        "clean code": "📗 متوفر حالياً في المكتبة",
        "python crash course": "📗 متوفر حالياً في المكتبة",
        "design patterns": "📕 غير متوفر حالياً",
        "the pragmatic programmer": "📗 متوفر حالياً في المكتبة",
    }
    
    text = str(value).strip().lower()
    
    if text in availability_map:
        return availability_map[text]
    
    return "❓ كتاب غير مسجل في النظام"