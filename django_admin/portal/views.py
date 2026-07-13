from django.http import JsonResponse

# 六大业务子系统（对应产品原型里的 6 个子页面）
MODULES = [
    {'key': 'tpm', 'name': 'TPM管理系统', 'desc': 'TPM 全员生产维护管理'},
    {'key': 'facility', 'name': '厂务管理数位化', 'desc': '厂务设施数字化管理'},
    {'key': 'quality', 'name': '品质分析系统', 'desc': '品质数据统计分析'},
    {'key': 'spare', 'name': '备品备件系统', 'desc': '备品备件库存管理'},
    {'key': 'motor', 'name': '电机监控系统', 'desc': '电机运行状态监控'},
    {'key': 'energy', 'name': '能源管理系统', 'desc': '能耗监测与管控'},
]


def index(request):
    """主页面 API：系统总览。前后端分离，只返回数据，页面由 Vue 渲染。
    当前数据库暂无数据，汇总指标统一用 '--' 占位。
    """
    data = {
        'title': '廊坊顶津智能管理系统',
        'summary': [
            {'label': '子系统', 'value': len(MODULES)},
            {'label': '在线设备', 'value': '--'},
            {'label': '今日报警', 'value': '--'},
            {'label': '待处理事项', 'value': '--'},
        ],
        'modules': MODULES,
    }
    return JsonResponse({'code': 0, 'msg': 'ok', 'data': data})
