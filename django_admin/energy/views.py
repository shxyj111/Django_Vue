from django.shortcuts import render


def index(request):
    return render(request, 'energy/index.html', {
        'active': 'energy',
        'name': '能源管理系统',
        'desc': '能耗监测与管控',
    })
