from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.shortcuts import render
# from django import models
import json
# 调用app_user数据库
from .models import User


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    username = request.POST.get('user')
    password = request.POST.get('pwd')

    user_object = User.objects.filter(username=username,password=password).first()
    if user_object:
        request.seesion["info"] = user_object.username
        # return render(request, 'success.html')
    else:
        return render(request, 'index.html', {'error': '用户名或密码错误'})

@csrf_exempt
def login(request):
    """登录接口：POST username/password，返回 token（校验数据库用户）"""
    if request.method != 'POST':
        return JsonResponse({'code': 405, 'msg': '仅支持 POST 请求'}, status=405)
    try:
        data = json.loads(request.body)
    except Exception:
        return JsonResponse({'code': 400, 'msg': '请求体不是合法 JSON'}, status=400)

    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return JsonResponse({'code': 401, 'msg': '用户名或密码不能为空'}, status=401)

    try:
        # 查找数据库
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'code': 401, 'msg': '用户不存在'}, status=401)

    if not check_password(password, user.password):
        return JsonResponse({'code': 401, 'msg': '用户名或密码错误'}, status=401)

    token = f'token-{username}-{user.id}'
    return JsonResponse({'code': 0, 'msg': '登录成功', 'data': {
        'token': token,
        'user': {
            'id': user.id,
            'username': user.username,
            'nickname': user.nickname,
            'role': user.role
        }
    }})


@csrf_exempt
def user_list(request):
    """用户列表接口：GET（直接查数据库）"""
    if request.method != 'GET':
        return JsonResponse({'code': 405, 'msg': '仅支持 GET 请求'}, status=405)
    users = list(User.objects.values('id', 'username', 'nickname', 'role'))
    return JsonResponse({'code': 0, 'msg': 'ok', 'data': {'list': users, 'total': len(users)}})


@csrf_exempt
def profile(request):
    """获取当前登录信息：需要 Authorization 头"""
    if request.method != 'GET':
        return JsonResponse({'code': 405, 'msg': '仅支持 GET 请求'}, status=405)
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        return JsonResponse({'code': 401, 'msg': '未登录或 token 缺失'}, status=401)
    return JsonResponse({'code': 0, 'msg': 'ok', 'data': {'token': auth[7:]}})
