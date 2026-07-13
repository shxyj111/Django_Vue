from django.shortcuts import render

# 六大业务子系统（对应产品原型里的 6 个子页面）
MODULES = [
    {'key': 'tpm', 'name': 'TPM管理系统', 'url': '/tpm/', 'desc': 'TPM 全员生产维护管理'},
    {'key': 'facility', 'name': '厂务管理数位化', 'url': '/facility/', 'desc': '厂务设施数字化管理'},
    {'key': 'quality', 'name': '品质分析系统', 'url': '/quality/', 'desc': '品质数据统计分析'},
    {'key': 'spare', 'name': '备品备件系统', 'url': '/spare/', 'desc': '备品备件库存管理'},
    {'key': 'motor', 'name': '电机监控系统', 'url': '/motor/', 'desc': '电机运行状态监控'},
    {'key': 'energy', 'name': '能源管理系统', 'url': '/energy/', 'desc': '能耗监测与管控'},
]


def index(request):
    """主页面：系统总览，展示 6 个子模块入口"""
    return render(request, 'portal/index.html', {'active': 'portal', 'modules': MODULES})
