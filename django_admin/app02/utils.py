"""工具函数集合（无状态、可复用，便于单测）。"""
import re


def generate_slug(title):
    """根据标题生成 slug（演示用，中文标题会做简单处理）。"""
    slug = re.sub(r'[^\w\s-]', '', title.lower()).strip()
    slug = re.sub(r'[\s]+', '-', slug)
    return slug[:120] or 'article'
