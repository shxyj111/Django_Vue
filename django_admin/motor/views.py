from django.http import JsonResponse


def index(request):
    """电机监控系统 API：前后端分离，只返回数据。暂无数据，用 '--' / 空列表占位。"""
    data = {
        'name': '电机监控系统',
        'desc': '电机运行状态监控',
        'stats': [
            {'label': '电机总数', 'value': '--'},
            {'label': '运行中', 'value': '--'},
            {'label': '故障数', 'value': '--'},
            {'label': '平均温度', 'value': '--'},
        ],
        'columns': ['电机编号', '电机名称', '运行状态', '温度', '电流'],
        'records': [],
    }
    return JsonResponse({'code': 0, 'msg': 'ok', 'data': data})
