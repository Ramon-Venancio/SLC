from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url="users:login")
def index(request):
    if request.method == 'POST':
        nome_categoria = request.POST['categoria']
        categoria = Category.objects.create(name=nome_categoria)
        categoria.save()

        nome_produto = request.POST['produto']
        produto = Product.objects.create(name=nome_produto)
        produto.save()

        categorias = Category.name.all()

        return render(request, 'task/index.html', {'categorias': categorias})
    
    return render(request, 'tasks/index.html')