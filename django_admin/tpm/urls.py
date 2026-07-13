from django.urls import path
from . import views

app_name = 'tpm'
urlpatterns = [
    path('', views.index, name='index'),
]
