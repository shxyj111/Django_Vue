from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# 演示数据（真实项目应从 MySQL 模型查询，例如 User.objects.all()）
MOCK_USERS = [
    {'id': 1, 'username': 'admin', 'nickname': '管理员', 'role': 'admin'},
    {'id': 2, 'username': 'alice', 'nickname': '爱丽丝', 'role': 'user'},
    {'id': 3, 'username': 'bob', 'nickname': '鲍勃', 'role': 'user'},
]


@csrf_exempt
def login(request):
    """登录接口：POST username/password，返回 token"""
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
    # 演示校验：真实项目应查询数据库并比对密码哈希
    if password != '123456':
        return JsonResponse({'code': 401, 'msg': '用户名或密码错误'}, status=401)
    user = next((u for u in MOCK_USERS if u['username'] == username), None)
    if not user:
        return JsonResponse({'code': 401, 'msg': '用户不存在'}, status=401)
    token = f'token-{username}-{user["id"]}'
    return JsonResponse({'code': 0, 'msg': '登录成功', 'data': {'token': token, 'user': user}})


@csrf_exempt
def user_list(request):
    """用户列表接口：GET"""
    if request.method != 'GET':
        return JsonResponse({'code': 405, 'msg': '仅支持 GET 请求'}, status=405)
    return JsonResponse({
        'code': 0, 'msg': 'ok',
        'data': {'list': MOCK_USERS, 'total': len(MOCK_USERS)}
    })


@csrf_exempt
def profile(request):
    """获取当前登录信息：需要 Authorization 头"""
    if request.method != 'GET':
        return JsonResponse({'code': 405, 'msg': '仅支持 GET 请求'}, status=405)
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        return JsonResponse({'code': 401, 'msg': '未登录或 token 缺失'}, status=401)
    return JsonResponse({'code': 0, 'msg': 'ok', 'data': {'token': auth[7:]}})
