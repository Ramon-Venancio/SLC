from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product,Category


@login_required(login_url="users:login")
def index(request):
    if request.method == 'POST':
        nome_categoria = request.POST['categoria']
        categoria = Category.objects.create(name=nome_categoria)
        categoria.save()

        return render(request, 'task/index.html', {'categorias': Category.objects.all()})
    
    return render(request, 'tasks/index.html')