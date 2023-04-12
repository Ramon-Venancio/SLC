from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

# Create your views here.

def cadastrar(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']
        
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse nome')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso')

    return render(request, 'users/cadastrar.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Nome ou senha invalidos!')
    return render(request, 'users/login.html')

def logout(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Você se desconectou'
    })