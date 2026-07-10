from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo_bilibili(request):
    return render(request, 'demo_bilibili.html')

def login(request):
    return HttpResponse('登录')