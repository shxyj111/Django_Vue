from django.shortcuts import render


def index(request):
    return render(request, 'quality/index.html', {
        'active': 'quality',
        'name': '品质分析系统',
        'desc': '品质数据统计分析',
    })
