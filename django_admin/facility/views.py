from django.shortcuts import render


def index(request):
    return render(request, 'facility/index.html', {
        'active': 'facility',
        'name': '厂务管理数位化',
        'desc': '厂务设施数字化管理',
    })
