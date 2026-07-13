from django.http import JsonResponse


def index(request):
    """能源管理系统 API：前后端分离，只返回数据。暂无数据，用 '--' / 空列表占位。"""
    data = {
        'name': '能源管理系统',
        'desc': '能耗监测与管控',
        'stats': [
            {'label': '今日总能耗', 'value': '--'},
            {'label': '用电', 'value': '--'},
            {'label': '用水', 'value': '--'},
            {'label': '用气', 'value': '--'},
        ],
        'columns': ['计量点', '能源类型', '本期用量', '同比', '采集时间'],
        'records': [],
    }
    return JsonResponse({'code': 0, 'msg': 'ok', 'data': data})
