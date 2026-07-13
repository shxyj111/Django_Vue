from django.urls import path
from . import views

app_name = 'motor'
urlpatterns = [
    path('', views.index, name='index'),
]
