from django.apps import AppConfig
from django.db.models.signals import post_migrate


class App01Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app01'

    def ready(self):
        # 迁移完成后自动执行种子数据
        from .signals import seed_default_users
        post_migrate.connect(seed_default_users, sender=self)
