from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from books.models import Book
from .models import Notification


@receiver(post_save, sender=Book)
def notify_users_when_book_is_created(
    sender,
    instance,
    created,
    **kwargs,
):
    if not created:
        return

    User = get_user_model()
    active_users = User.objects.filter(is_active=True)

    for user in active_users:
        Notification.objects.create(
            recipient=user,
            title="كتاب جديد أُضيف إلى المكتبة",
            message=f"تمت إضافة الكتاب: {instance.title}",
        )

        if user.email:
            send_mail(
                subject="كتاب جديد في مكتبتي الرقمية",
                message=(
                    f"مرحبًا {user.username}،\n\n"
                    f"تمت إضافة كتاب جديد إلى المكتبة: {instance.title}.\n"
                    f"المؤلف: {instance.author}\n"
                    f"السعر: {instance.price}\n"
                ),
                from_email=None,
                recipient_list=[user.email],
                fail_silently=True,
            )