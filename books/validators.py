from django.core.exceptions import ValidationError


def validate_book_title(value):
    normalized_title = " ".join(str(value).split())

    if len(normalized_title) < 3:
        raise ValidationError(
            "يجب أن يحتوي عنوان الكتاب على ثلاثة أحرف أو أكثر."
        )

    if not any(character.isalnum() for character in normalized_title):
        raise ValidationError(
            "يجب أن يحتوي عنوان الكتاب على أحرف أو أرقام."
        )