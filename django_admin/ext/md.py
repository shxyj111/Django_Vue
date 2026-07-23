from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 登录页面和登录 API 放行
        if request.path_info in ['/index/', '/api/login/']:
            return

        # 前后端分离的 API 接口：不在 session 中间件里校验，由视图函数自行校验 token
        if request.path_info.startswith('/api/'):
            return

        # 其余服务端渲染页面仍按原来的 session 校验
        info_dict = request.session.get("info")
        # 如果目前这个网页中的session中有值，那么就进入到网页中
        if info_dict:

            # 给request对象增加一个属性，这样可以快速从请求参数中获取到需要重复获取的那部分用户信息
            request.info_dict = info_dict
            return

        return redirect("/index/")
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('process_view')
        return None