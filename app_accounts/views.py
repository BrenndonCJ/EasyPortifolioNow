from typing import Any
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import View

from . import models

from easyportfolionow.mydecorators import LogoutRequiredMixin

from random import randint

# Create your views here.
class CadastroView(LogoutRequiredMixin, View):
    def __init__(self, procfile_url='/portfolio/perfil/') -> None:
        super().__init__(procfile_url)
    
    def get(self, request):
        return render(request=request, template_name='app_accounts/cadastro.html', context={"title":"EasyPortfolioNow | Cadastro"})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if (len(str(username)) < 1) or (len(str(password)) < 1) or (len(str(email)) < 1):
            messages.add_message(request, constants.INFO, f"Preencha os campos corretamente")
            return render(request=request, template_name='app_accounts/cadastro.html')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            perfil = models.Perfil.objects.create(
                user=user,
            )
            perfil.save()
        except:
            name_sugestion = randint(1000,9999)
            name_sugestion = username + str(name_sugestion)
            messages.add_message(request, constants.ERROR, 'Nome de Usuario indisponivel')
            messages.add_message(request, constants.INFO, f"Tente: {name_sugestion}")
            return render(request=request, template_name='app_accounts/cadastro.html')

        if user:
            user = authenticate(
                username=username,
                password=password,
            )
            
            login(request, user)
            return redirect("userperfil")
        else:
            messages.add_message(request, constants.ERROR, 'Nome de Usuario indisponivel')
            return render(request=request, template_name='app_accounts/cadastro.html')

class LoginView(LogoutRequiredMixin, View):
    def __init__(self, procfile_url='/portfolio/perfil/') -> None:
        super().__init__(procfile_url)
    
    def get(self, request):
        return render(request=request, template_name='app_accounts/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return redirect("userperfil")
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha incorretos')
            return render(request=request, template_name='app_accounts/login.html')

@login_required(login_url='/')
def sair(request):
    logout(request)
    return redirect('index')
