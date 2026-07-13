from django.shortcuts import render


def index(request):
    return render(request, 'spare/index.html', {
        'active': 'spare',
        'name': '备品备件系统',
        'desc': '备品备件库存管理',
    })
