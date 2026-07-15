"""后台注册 —— 企业级必做，让运营/管理员可在 /admin 管理数据。

官方文档：https://docs.djangoproject.com/en/5.2/ref/contrib/admin/
"""
from django.contrib import admin
from .models import Category, Article, Author, AuthorProfile, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'status', 'category', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'content')
    raw_id_fields = ('category',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'phone')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
