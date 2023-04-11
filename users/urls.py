from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar', views.index, name='cadastrar'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
