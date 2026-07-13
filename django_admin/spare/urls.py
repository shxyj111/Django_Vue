from django.urls import path
from . import views

app_name = 'spare'
urlpatterns = [
    path('', views.index, name='index'),
]
