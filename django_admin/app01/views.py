from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
# from django import models
import json
# 调用app_user数据库
from .models import User, UserInfo


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    user_object = UserInfo.objects.filter(username=username).first()
    if user_object:
        # 情况1：密码已是哈希格式，直接校验
        if check_password(password, user_object.password):
            request.session["info"] = {"name": user_object.username, "id": user_object.id}
            return redirect("/home/")
        # 情况2：兼容旧明文密码——明文匹配成功后自动升级为哈希存储
        elif user_object.password == password:
            user_object.password = make_password(password)
            user_object.save()
            request.session["info"] = {"name": user_object.username, "id": user_object.id}
            return redirect("/home/")
    # 用户名不存在或密码错误
    return render(request, 'index.html', {'error': '用户名或密码错误'})
    
def home(request):
    # 判断用户是否已经登陆过(cookie校验)，如果没有登陆过就不给进入home界面，而是直接回退到登录界面
    # 这个request是中间件发过来的请求，而中间件也会接收上一个请求，而每次网页有变动都会走一边中间件，所以这里的request指的是所有中间件走完或者是特殊中间件导致提前截止时的所有请求信息的集合
    info_dict = request.info_dict
    return render(request, 'home.html',{"info":info_dict})

def layout(request):
    return render(request, 'layout.html')

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

    # 情况1：密码已是哈希格式，直接校验
    if check_password(password, user.password):
        pass
    # 情况2：兼容旧明文密码——明文匹配成功后自动升级为哈希存储
    elif user.password == password:
        user.password = make_password(password)
        user.save()
    else:
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
