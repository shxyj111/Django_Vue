"""常量与枚举定义（推荐用 TextChoices 替代裸字符串 choices）。

官方文档：https://docs.djangoproject.com/en/5.2/ref/models/fields/#enumeration-types
"""
from django.db import models


class ArticleStatus(models.TextChoices):
    DRAFT = 'draft', '草稿'
    PUBLISHED = 'published', '已发布'
    ARCHIVED = 'archived', '已归档'
