from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request,'cadastro.html')
    elif request.method == "POST":
        #as strings devem ter o mesmo nome definido para os itens no arq partials/cadastro.html
        username = request.POST.get('username') 
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if not senha == confirmar_senha:
            messages.add_message(request,constants.ERROR,'As senhas informadas não coincidem. Por favor, confirme a senha')
            return redirect(reverse('cadastro')) #redireciona o usuario para a tela de cadastro novamente
       
        user = User.objects.filter(username=username)
        if user.exists(): #verifica se um usuário já existe no banco
            messages.add_message(request,constants.ERROR,'Este usuário não está disponivel')
            return redirect(reverse('cadastro'))
                 
        #cria o usuário no banco de dados
        #a senha já será criptografada automaticamente com o algoritmo pbkdf_2(um dos algoritmos mais forte de hashing)
        user = User.objects.create_user(username=username,email=email,password=senha)
        user.save()
        messages.add_message(request,constants.SUCCESS,'Usuário Cadastrado com sucesso!')

        return redirect(reverse('login'))

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        #verifica se o usuário existe, se ele existir é retornado
        user = auth.authenticate(username = username, password = senha)

        if not (user):
            messages.add_message(request,constants.ERROR,'Usuário não encontrado')
            return redirect(reverse('login'))
        
        auth.login(request,user)
        return redirect('eventos/new_event/')
