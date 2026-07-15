from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.relation_demo),
    path('advanced/', views.advanced_demo),
]
