"""自定义验证器 —— 在模型层保证数据合法性，可复用于表单/序列化器。

官方文档：https://docs.djangoproject.com/en/5.2/ref/validators/
"""
import re
from django.core.exceptions import ValidationError


def validate_phone(value):
    """校验中国大陆手机号。空值放行（字段本身 blank=True 控制必填）。"""
    if value and not re.match(r'^1[3-9]\d{9}$', value):
        raise ValidationError('%(value)s 不是合法的手机号', params={'value': value})
