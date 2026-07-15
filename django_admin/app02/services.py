"""写操作层（Service Layer）—— 把"创建/修改"业务逻辑从视图抽离，
用事务包裹保证一致性，视图/API/管理命令都能复用同一份逻辑。

参考 Django 风格指南（hacksoft django-styleguide）：
https://github.com/HackSoftware/Django-Styleguide
"""
from django.db import transaction
from .models import Article, Tag


@transaction.atomic
def create_article(*, title, category, content='', tag_names=None, status='draft'):
    """创建文章并（可选）关联标签，整体在一个事务里。"""
    article = Article.objects.create(
        title=title,
        content=content,
        category=category,
        status=status,
    )
    if tag_names:
        tags = [Tag.objects.get_or_create(name=name)[0] for name in tag_names]
        article.tags.set(tags)
    return article


@transaction.atomic
def publish_article(article_id):
    """发布文章：用 select_for_update 加行锁，避免并发竞态。"""
    article = Article.objects.select_for_update().get(id=article_id)
    article.status = 'published'
    article.save(update_fields=['status'])
    return article
