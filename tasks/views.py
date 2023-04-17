from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product,Category
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url="users:login")
def index(request, categoria_id=0):   
    return render(request, 'tasks/index.html', {
        'categorias': Category.objects.all(),
        'categoria_id': categoria_id
        })


def criar_categoria(request):
    if request.method == 'POST':
        nome_categoria = request.POST['categoria']
        categoria = Category.objects.create(name=nome_categoria)
        categoria.save()

        return HttpResponseRedirect(reverse("tasks:index"))

def criar_produto(request, categoria_id):
    if request.method == 'POST':
        nome_produto = request.POST['produto']
        quantidade = request.POST['quantidade']
        produto = Product.objects.create(name=nome_produto, quantidade=quantidade)
        produto.save()

        categoria = Category.objects.get(id=categoria_id)

        produto.categorias.add(categoria)

        return HttpResponseRedirect(reverse("tasks:index", args=(categoria_id)))    