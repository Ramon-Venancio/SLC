from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.http import HttpResponseRedirect
from django.urls import reverse

# Função para cadastrar usuario:
def cadastrar(request):
    if request.method == 'POST':
        # Pegando os valores dados pelo html "cadastrar.html":
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']
        
        # Verificando se o usuario já existe:
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuário com esse nome')
        
        # Criando um usuario:
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return render(request, 'users/login.html', {'message': 'Usuário cadastrado com sucesso'})

    return render(request, 'users/cadastrar.html')

# Função para efetuar o login do usuario:
def login(request):
    if request.method == 'POST':
        # Pegando os valores dados pelo html "login.html":
        username = request.POST['username']
        senha = request.POST['senha']

        # Verificando o usuario:
        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user) # Logando o usuario
            return HttpResponseRedirect(reverse('tasks:index'))

        else:
            return render(request, 'users/login.html', {'message': 'Nome ou senha invalidos!'})
    return render(request, 'users/login.html')

# Função para deslogar o usuario:
def logout(request):
    logout_django(request) # Deslogando o usuario
    return render(request, 'users/login.html', {
        'message': 'Você se desconectou'
    })