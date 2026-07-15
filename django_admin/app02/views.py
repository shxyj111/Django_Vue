from django.http import HttpResponse
from .models import Category, Article, Author, AuthorProfile, Tag
from .constants import ArticleStatus
from .services import create_article, publish_article
from .selectors import get_published_articles


def relation_demo(request):
    """演示表与表之间关联关系的各种 ORM 操作。

    访问 http://127.0.0.1:8000/app02/demo/ 即可看到运行结果。
    每次访问都会用 get_or_create 复用已有数据，避免重复创建。
    """
    lines = []
    L = lines.append

    # ---------- 准备演示数据 ----------
    cat_python, _ = Category.objects.get_or_create(name='Python')
    cat_django, _ = Category.objects.get_or_create(name='Django')

    a1, _ = Article.objects.get_or_create(title='Django入门', defaults={'content': '...'})
    a1.category = cat_django
    a1.save()
    a2, _ = Article.objects.get_or_create(title='Python基础', defaults={'content': '...'})
    a2.category = cat_python
    a2.save()

    tag_web, _ = Tag.objects.get_or_create(name='Web')
    tag_basic, _ = Tag.objects.get_or_create(name='基础')
    a1.tags.add(tag_web)                 # 文章1 关联 Web
    a2.tags.add(tag_basic, tag_web)      # 文章2 关联 基础 + Web

    author, _ = Author.objects.get_or_create(name='张三')
    profile, _ = AuthorProfile.objects.get_or_create(
        author=author, defaults={'bio': '资深开发', 'phone': '13800000000'}
    )

    # ---------- 1. 一对多 ForeignKey ----------
    L('===== 1. 一对多 ForeignKey =====')
    L(f'正向：文章《{a1.title}》所属分类 = {a1.category.name}')
    L(f'反向：分类「{cat_django.name}」下的文章 = '
      f'{[x.title for x in cat_django.articles.all()]}')
    L(f'跨表过滤：category__name="Django" 的文章 = '
      f'{[x.title for x in Article.objects.filter(category__name="Django")]}')

    # ---------- 2. 一对一 OneToOneField ----------
    L('')
    L('===== 2. 一对一 OneToOneField =====')
    L(f'正向：作者 {author.name} 的简介 = {author.profile.bio}')
    L(f'反向：简介「{profile.bio}」对应的作者 = {profile.author.name}')

    # ---------- 3. 多对多 ManyToManyField ----------
    L('')
    L('===== 3. 多对多 ManyToManyField =====')
    L(f'正向：文章《{a1.title}》的标签 = {[t.name for t in a1.tags.all()]}')
    L(f'反向：标签「{tag_web.name}」下的文章 = '
      f'{[x.title for x in tag_web.articles.all()]}')
    a1.tags.remove(tag_web)
    L(f'remove 后：《{a1.title}》的标签 = {[t.name for t in a1.tags.all()]}')
    a1.tags.add(tag_web)
    L(f'add 后：《{a1.title}》的标签 = {[t.name for t in a1.tags.all()]}')
    a1.tags.set([tag_web])
    L(f'set([Web]) 后：《{a1.title}》的标签 = {[t.name for t in a1.tags.all()]}')
    a1.tags.clear()
    L(f'clear 后：《{a1.title}》的标签 = {[t.name for t in a1.tags.all()]}')
    a1.tags.add(tag_web, tag_basic)

    # ---------- 4. 关联查询优化 ----------
    L('')
    L('===== 4. 关联查询优化（避免 N+1 查询） =====')
    L('select_related：用于 FK / O2O 正向，一次性 SQL JOIN')
    L('  Article.objects.select_related("category")')
    L('prefetch_related：用于 M2M / 反向关联，分别查询后在内存中关联')
    L('  Article.objects.prefetch_related("tags")')

    html = '<pre style="font-size:14px;line-height:1.6">' + '\n'.join(lines) + '</pre>'
    return HttpResponse(html)


def advanced_demo(request):
    """演示企业级推荐模块：services / selectors / managers / signals / validators。"""
    lines = []
    L = lines.append

    # services：事务创建文章 + 标签（slug 由信号自动生成）
    cat, _ = Category.objects.get_or_create(name='Django')
    article = create_article(
        title='用 Service 创建的文章',
        category=cat,
        content='演示 service layer',
        tag_names=['Web', '最佳实践'],
        status=ArticleStatus.DRAFT,
    )
    L('===== services（写操作/事务层） =====')
    L(f'create_article -> {article.title}')
    L(f'  status={article.status}, slug={article.slug}（信号自动生成）')
    L(f'  tags={[t.name for t in article.tags.all()]}')

    # selectors：语义化查询
    L('')
    L('===== selectors（读操作层） =====')
    published = get_published_articles()
    L(f'get_published_articles() -> {[a.title for a in published]}')

    # managers：自定义查询
    L('')
    L('===== managers（自定义 QuerySet/Manager） =====')
    L(f'Article.objects.drafts() -> {[a.title for a in Article.objects.drafts()]}')
    L('Article.objects.published().with_category().with_tags() 已预取关联')

    # services：发布（事务 + 行锁）
    L('')
    L('===== 事务发布 =====')
    publish_article(article.id)
    L(f'publish_article({article.id}) -> '
      f'status={Article.objects.get(id=article.id).status}')

    # validators：触发校验
    L('')
    L('===== validators（自定义验证器） =====')
    try:
        p = AuthorProfile(author=Author.objects.get_or_create(name='测试用户')[0], phone='123')
        p.full_clean()
    except Exception as e:
        L(f'validate_phone 拦截了非法手机号「123」：{list(e.messages)}')

    html = '<pre style="font-size:14px;line-height:1.6">' + '\n'.join(lines) + '</pre>'
    return HttpResponse(html)
