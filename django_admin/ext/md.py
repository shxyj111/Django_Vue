from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 如果是登录的页面的话就跳过
        if request.path_info == '/index/':
            return
        
        # 除了登录页面以外的页面都需要做验证
        info_dict = request.session.get("info")
        if info_dict:

            # 给request对象增加一个属性，这样可以快速获取到需要重复获取的那部分用户信息
            request.info_dict = info_dict
            return 
        
        return redirect("/index/")
    
    def process_view(self, response, request):
        print('process_view')
        return response