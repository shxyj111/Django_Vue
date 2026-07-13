from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nickname', 'role', 'created_at')
    list_filter = ('role',)
    search_fields = ('username', 'nickname')

    def save_model(self, request, obj, form, change):
        # 保存时对密码做哈希，避免明文存储（生产必备）
        if obj.password:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
