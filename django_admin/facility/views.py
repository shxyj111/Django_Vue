from django.http import JsonResponse


def index(request):
    """厂务管理数位化 API：前后端分离，只返回数据。暂无数据，用 '--' / 空列表占位。"""
    data = {
        'name': '厂务管理数位化',
        'desc': '厂务设施数字化管理',
        'stats': [
            {'label': '今日用水量', 'value': '--'},
            {'label': '今日用电量', 'value': '--'},
            {'label': '空调机组', 'value': '--'},
            {'label': '报警数', 'value': '--'},
        ],
        'columns': ['设备编号', '设施名称', '运行状态', '所在区域', '更新时间'],
        'records': [],
    }
    return JsonResponse({'code': 0, 'msg': 'ok', 'data': data})
