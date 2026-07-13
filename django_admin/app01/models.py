from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ('admin', '管理员'),
        ('user', '普通用户'),
    ]
    username = models.CharField(max_length=50, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user', verbose_name='角色')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.nickname or self.username
