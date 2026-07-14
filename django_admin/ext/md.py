from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class MyMiddleware(MiddlewareMixin):


    

    def process_request(self, request):

        # 如果是登录的页面的话就跳过
        if request.path_info == '/index/':
            return
        
        # 除了登录页面以外的页面都需要做验证
        info_dict = request.session.get("info")
        if not info_dict:
            return 
        
        return redirect("/index/")
    
    def process_view(self, response, request):
        print('process_view')
        return response