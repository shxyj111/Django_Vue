from django.contrib import admin
from django.urls import path
from app01 import views as app01_views

urlpatterns = [
    # API 接口（均带 /api 前缀，与前端代理规则对应）
    path('api/login/', app01_views.login),
    path('api/users/', app01_views.user_list),
    path('api/profile/', app01_views.profile),
    # Django 自带后台
    path('admin/', admin.site.urls),
]
