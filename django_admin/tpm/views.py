from django.http import JsonResponse


def index(request):
    """TPM管理系统 API：前后端分离，只返回数据。暂无数据，用 '--' / 空列表占位。"""
    data = {
        'name': 'TPM管理系统',
        'desc': 'TPM 全员生产维护管理',
        'stats': [
            {'label': '设备总数', 'value': '--'},
            {'label': '保养计划', 'value': '--'},
            {'label': '待处理工单', 'value': '--'},
            {'label': '完成率', 'value': '--'},
        ],
        'columns': ['设备编号', '设备名称', '保养状态', '负责人', '最近保养'],
        'records': [],
    }
    return JsonResponse({'code': 0, 'msg': 'ok', 'data': data})
