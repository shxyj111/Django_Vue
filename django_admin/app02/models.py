from django.db import models
from .constants import ArticleStatus
from .validators import validate_phone
from .managers import ArticleManager


# ============================================================
# 演示：一对多  ForeignKey
#   一个分类(Category)下有多篇文章(Article)
# ============================================================
class Category(models.Model):
    """分类（一）"""
    name = models.CharField(max_length=50, verbose_name='分类名称')

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章（多）"""
    title = models.CharField(max_length=100, verbose_name='标题')
    slug = models.SlugField(max_length=120, blank=True, verbose_name='slug')
    content = models.TextField(blank=True, verbose_name='内容')
    status = models.CharField(
        max_length=10,
        choices=ArticleStatus.choices,   # 用 TextChoices 枚举，而非裸字符串
        default=ArticleStatus.DRAFT,
        verbose_name='状态',
    )
    # 一对多：多篇文章属于一个分类
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='分类',
    )
    # 多对多：一篇文章有多个标签，一个标签可对应多篇文章
    tags = models.ManyToManyField(
        'Tag',
        related_name='articles',
        blank=True,
        verbose_name='标签',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    objects = ArticleManager()   # 使用自定义管理器（封装常用查询）

    def __str__(self):
        return self.title


# ============================================================
# 演示：一对一  OneToOneField
#   给作者(Author)做扩展信息(AuthorProfile)
# ============================================================
class Author(models.Model):
    """作者"""
    name = models.CharField(max_length=50, verbose_name='姓名')

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    """作者详情（一对一扩展）"""
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='作者',
    )
    bio = models.TextField(blank=True, verbose_name='简介')
    phone = models.CharField(
        max_length=11,
        blank=True,
        validators=[validate_phone],   # 自定义验证器
        verbose_name='电话',
    )

    def __str__(self):
        return f'{self.author.name} 的资料'


# ============================================================
# 演示：多对多  ManyToManyField 的从表
# ============================================================
class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=30, verbose_name='标签名')

    def __str__(self):
        return self.name
