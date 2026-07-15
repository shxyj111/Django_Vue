"""自定义 Manager / QuerySet —— 把常用查询封装在模型层，视图只调用语义化方法。

官方文档：
- Manager:  https://docs.djangoproject.com/en/5.2/topics/db/managers/
- QuerySet: https://docs.djangoproject.com/en/5.2/ref/models/querysets/
"""
from django.db import models


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='published')

    def drafts(self):
        return self.filter(status='draft')

    def with_category(self):
        return self.select_related('category')

    def with_tags(self):
        return self.prefetch_related('tags')


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    # 把 QuerySet 上的方法也暴露到 Manager，方便 Article.objects.published()
    def published(self):
        return self.get_queryset().published()

    def drafts(self):
        return self.get_queryset().drafts()

    def with_category(self):
        return self.get_queryset().with_category()

    def with_tags(self):
        return self.get_queryset().with_tags()
