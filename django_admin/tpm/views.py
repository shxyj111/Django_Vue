from django.shortcuts import render


def index(request):
    return render(request, 'tpm/index.html', {
        'active': 'tpm',
        'name': 'TPM管理系统',
        'desc': 'TPM 全员生产维护管理',
    })
