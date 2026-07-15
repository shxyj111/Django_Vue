from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Category, Article
from .services import create_article
from .validators import validate_phone


class ArticleServiceTests(TestCase):
    def test_create_article_creates_tags(self):
        cat = Category.objects.create(name='Python')
        article = create_article(
            title='测试文章', category=cat, tag_names=['Web', '基础'],
        )
        self.assertEqual(article.tags.count(), 2)
        self.assertEqual(article.status, 'draft')
        self.assertTrue(article.slug)  # 信号自动生成 slug

    def test_validate_phone_rejects_bad(self):
        with self.assertRaises(ValidationError):
            validate_phone('123')
