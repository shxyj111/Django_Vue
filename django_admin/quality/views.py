from django.http import JsonResponse


def index(request):
    """品质分析系统 API：前后端分离，只返回数据。暂无数据，用 '--' / 空列表占位。"""
    data = {
        'name': '品质分析系统',
        'desc': '品质数据统计分析',
        'stats': [
            {'label': '检测批次', 'value': '--'},
            {'label': '合格率', 'value': '--'},
            {'label': '不良数', 'value': '--'},
            {'label': '待复检', 'value': '--'},
        ],
        'columns': ['批次号', '产品名称', '检测项', '结果', '检测时间'],
        'records': [],
    }
    return JsonResponse({'code': 0, 'msg': 'ok', 'data': data})
