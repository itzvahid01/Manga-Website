import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def validate_iranian_phone_number(value):
    """
    Validates that the given value is a valid Iranian phone number.
    """
    # الگوی Regex برای شماره‌های ایرانی
    iran_phone_regex = r'^09\d{9}$'
    if not re.match(iran_phone_regex, value):
        raise ValidationError(
            _('شماره تلفن وارد شده معتبر نیست. لطفاً یک شماره تلفن ایرانی وارد کنید.'),
            code='invalid_phone_number'
        )