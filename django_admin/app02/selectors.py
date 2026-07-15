"""读操作层（Selector Layer）—— 封装复杂查询，视图/API 只调用语义化方法，
避免把 ORM 细节散落在各个视图里。

参考：https://github.com/HackSoftware/Django-Styleguide
"""
from .models import Article


def get_published_articles():
    """返回已发布文章，并预先关联分类与标签（避免 N+1 查询）。"""
    return Article.objects.published().with_category().with_tags()


def get_article_detail(article_id):
    return Article.objects.with_category().with_tags().get(id=article_id)
