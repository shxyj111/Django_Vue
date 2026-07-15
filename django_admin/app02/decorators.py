"""自定义视图装饰器 —— 把横切逻辑（限流、鉴权、方法限制）与业务解耦。"""
from functools import wraps
from django.http import JsonResponse


def require_post(view_func):
    """只允许 POST 方法的装饰器。"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.method != 'POST':
            return JsonResponse({'error': '仅支持 POST 请求'}, status=405)
        return view_func(request, *args, **kwargs)
    return wrapper
