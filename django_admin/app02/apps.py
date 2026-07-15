from django.apps import AppConfig


class App02Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app02'

    def ready(self):
        # 导入信号模块，确保信号接收器被注册（否则 pre_save 不会触发）
        from . import signals  # noqa: F401
