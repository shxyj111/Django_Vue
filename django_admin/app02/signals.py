"""信号 —— 在模型保存前后自动执行副作用（如自动生成 slug）。

官方文档：https://docs.djangoproject.com/en/5.2/topics/signals/
注意：信号必须在 AppConfig.ready() 中 import 才会被注册（见 apps.py）。
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Article
from .utils import generate_slug


@receiver(pre_save, sender=Article)
def auto_slug(sender, instance, **kwargs):
    """保存文章时，若 slug 为空则自动生成。"""
    if not instance.slug:
        instance.slug = generate_slug(instance.title)
