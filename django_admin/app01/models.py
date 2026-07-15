from django.db import models


# 由于这里是在app01下models.py文件中创建的表，所以实际上这个新建表的名称是app01+User
class User(models.Model):
    ROLE_CHOICES = [
        ('admin', '管理员'),
        ('user', '普通用户'),
    ]
    username = models.CharField(max_length=50, unique=True, verbose_name='用户名')
    # 这里最大长度为128是因为要存储加密后的哈希密码
    password = models.CharField(max_length=128, verbose_name='密码')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user', verbose_name='角色')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.nickname or self.username

class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    # 长度改为128以存储 Django 的哈希密码（如 pbkdf2_sha256$...）
    password = models.CharField(max_length=128, verbose_name='密码')
    age = models.IntegerField(verbose_name='年龄')
    mobile = models.CharField(max_length=11, verbose_name='手机号')

# class 