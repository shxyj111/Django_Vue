from django.shortcuts import render


def index(request):
    return render(request, 'motor/index.html', {
        'active': 'motor',
        'name': '电机监控系统',
        'desc': '电机运行状态监控',
    })
