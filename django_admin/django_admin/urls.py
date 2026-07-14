from django.contrib import admin
from django.urls import path, include
from app01 import views as app01_views

urlpatterns = [
    # API 接口（均带 /api 前缀，与前端代理规则对应）
    path('api/login/', app01_views.login),
    path('api/users/', app01_views.user_list),
    path('api/profile/', app01_views.profile),
    # 七个业务页面已改为前后端分离：Django 只提供数据 API，页面由 Vue 渲染
    # 主页面（系统总览）
    path('api/portal/', include('portal.urls')),
    # 六个子页面
    path('api/tpm/', include('tpm.urls')),
    path('api/facility/', include('facility.urls')),
    path('api/quality/', include('quality.urls')),
    path('api/spare/', include('spare.urls')),
    path('api/motor/', include('motor.urls')),
    path('api/energy/', include('energy.urls')),
    # Django 自带后台
    path('admin/', admin.site.urls),

    path('index/', app01_views.index),
    path('home/', app01_views.home),
]
