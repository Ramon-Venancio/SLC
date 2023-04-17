from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('criado_categoria', views.criar_categoria, name='criar_categoria'),
    path('<int:categoria_id>/criado_produto', views.criar_produto, name='criar_produto'),
    path('<int:produto_id>/deletado_produto',views.deletar_produto, name='deletar_produto'),
    path('<int:categoria_id>/deletado_categoria', views.deletar_categoria, name='deletar_categoria')
]