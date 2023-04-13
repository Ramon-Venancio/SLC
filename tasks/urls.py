from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('index.html', views.index, name='index'),
]