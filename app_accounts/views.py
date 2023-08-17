from typing import Any
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import View

from easyportfolionow.mydecorators import LogoutRequiredMixin

# Create your views here.
class CadastroView(LogoutRequiredMixin, View):
    def __init__(self, procfile_url='/') -> None:
        super().__init__(procfile_url)
    
    def get(self, request):
        return render(request=request, template_name='app_accounts/cadastro.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        return HttpResponse(200)
    
def cadastro(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        return HttpResponse(200)
    
    context = {
        "title":"CADASTRO",
        "imageurl":"/media/bg.jpg"
    }
    return render(request=request, template_name='app_accounts/cadastro.html', context=context)

def logar(request):
    return render(request=request, template_name='app_accounts/login.html')

def sair(request):
    return HttpResponse(200)
