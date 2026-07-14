from django.apps import AppConfig
from django.db.models.signals import post_migrate


class App01Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app01'

    def ready(self):
        # 迁移完成后自动执行种子数据
        from .signals import seed_default_users
        # 这个的作用是在使用makemigrations(读取所有已注册的app来生成计划书到migrations文件夹) 和migrate命令后，根据后者的结束广播来从apps.py中执行.signals.py中的函数seed_default_users,以此来写入三个演示账号
        post_migrate.connect(seed_default_users, sender=self)
