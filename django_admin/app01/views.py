from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def demo_bilibili(request):
    return render(request, 'demo_bilibili.html')

def login(request):
    # 返回 JSON 数据给前端 Vue 调用
    return JsonResponse({'code': 0, 'msg': '登录成功', 'data': {}})