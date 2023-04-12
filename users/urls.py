from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login.html', views.login, name='login'),
    path('cadastrar.html', views.cadastrar, name='cadastro'),
    path('logout', views.logout, name='logout'),
]
