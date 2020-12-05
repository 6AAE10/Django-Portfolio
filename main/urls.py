from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ru/', views.index_ru, name='ru')
]