from django.contrib.auth.hashers import make_password
from .models import User


def seed_default_users(sender, **kwargs):
    """迁移后自动写入演示账号（幂等：已存在则跳过）"""
    defaults = [
        ('admin', '123456', '管理员', 'admin'),
        ('alice', '123456', '爱丽丝', 'user'),
        ('bob', '123456', '鲍勃', 'user'),
    ]
    for username, password, nickname, role in defaults:
        if not User.objects.filter(username=username).exists():
            User.objects.create(
                username=username,
                password=make_password(password),
                nickname=nickname,
                role=role
            )
