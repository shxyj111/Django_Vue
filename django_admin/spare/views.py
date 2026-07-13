from django.http import JsonResponse


def index(request):
    """备品备件系统 API：前后端分离，只返回数据。暂无数据，用 '--' / 空列表占位。"""
    data = {
        'name': '备品备件系统',
        'desc': '备品备件库存管理',
        'stats': [
            {'label': '备件种类', 'value': '--'},
            {'label': '库存总量', 'value': '--'},
            {'label': '低库存预警', 'value': '--'},
            {'label': '本月出库', 'value': '--'},
        ],
        'columns': ['备件编号', '备件名称', '规格', '库存数量', '存放位置'],
        'records': [],
    }
    return JsonResponse({'code': 0, 'msg': 'ok', 'data': data})
