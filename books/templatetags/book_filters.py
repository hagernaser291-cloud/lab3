from django import template

register = template.Library()

@register.filter(name='book_status')
def book_status(value):
    """
    فلتر مخصص لمشروع المكتبة يحول حالة الكتاب أو وصفه إلى نص تنسيقي مشجع
    """
    dictionary = {
        "متوفر": "📗 متوفر حالياً في المكتبة",
        "غير متوفر": "📕 غير متوفر حالياً",
        "جديد": "⭐ إصدار جديد مميز",
    }
    
    text = str(value)
    for key, replacement in dictionary.items():
        text = text.replace(key, replacement)
        
    return text