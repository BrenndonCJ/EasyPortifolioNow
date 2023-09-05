from typing import Any
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import View, ListView, CreateView, DeleteView
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from app_accounts import models
from random import randint


# Create your views here.
class PortfolioView(View):
    def get(self, request, username):
        try:
            perfil = models.Perfil.objects.get(user__username=username)
        
            if perfil:
                projetos = models.UsersProjects.objects.filter(user__id=perfil.user.id).order_by('id')
                context = {
                    'projetos':projetos,
                    'sociais':{
                        'instagram':perfil.instagram,
                        'twitter':perfil.twitter,
                        'github':perfil.github,
                        'tiktok':perfil.tiktok,
                        'linkedin':perfil.linkedin,
                    },
                    'frase':perfil.frase,
                    'descricao':perfil.sobre,
                    'portfolio_url':perfil.portfolio
                }
                return render (request=request, template_name="app_portfolio/modelo_0.html", context=context)
        except:
            return redirect("index")

class PortfolioCreate(LoginRequiredMixin,View):
    
    def get(self, request, modelo):
        perfil = models.Perfil.objects.get(user=request.user)
        
        if modelo:
            projetos = models.UsersProjects.objects.filter(user__id=request.user.id).order_by('id')
            context = {
                'projetos':projetos,
                'sociais':{
                    'instagram':perfil.instagram,
                    'twitter':perfil.twitter,
                    'github':perfil.github,
                    'tiktok':perfil.tiktok,
                    'linkedin':perfil.linkedin,
                },
                'frase':perfil.frase,
                'descricao':perfil.sobre,
            }
            return render (request=request, template_name="app_portfolio/modelo_0.html", context=context)
        else:
            return redirect("portfolioselect")

@login_required(login_url='account/logar')        
def generate_link(request, username):
    perfil = models.Perfil.objects.get(user=request.user)
    perfil.portfolio = request.build_absolute_uri(reverse("portfolioview", args=[str(username)]))
    perfil.save()
    return redirect("userperfil")

class PortfolioModelSelect(LoginRequiredMixin,View):
    def __init__(self, **kwargs: Any) -> None:
        self.template_name = "app_portfolio/selectportfolio.html"

    def get(self, request):
        
        context={
            'modelo0':0,
            'modelo1':1,
        }
        return render(request=request, template_name=self.template_name, context=context)
    
    def post(self, request, username):

        return HttpResponse(201)
    
class PerfilView(LoginRequiredMixin,View):

    def get(self, request):
        perfil = models.Perfil.objects.get(user=request.user)
        projetos = models.UsersProjects.objects.filter(user__id=request.user.id).order_by('id')
        context = {
            'projetos':projetos,
            'sociais':{
                'instagram':perfil.instagram,
                'twitter':perfil.twitter,
                'github':perfil.github,
                'tiktok':perfil.tiktok,
                'linkedin':perfil.linkedin,
                'frase':perfil.frase,
                'descricao':perfil.sobre,
            },
            "portfolio_url":perfil.portfolio
        }

        return render(request=request, template_name='app_portfolio/perfil.html', context=context)
    
    def post(self, request):
        try:
            instagram = request.POST.get("instagram")
            twitter = request.POST.get("twitter")
            github = request.POST.get("github")
            tiktok = request.POST.get("tiktok")
            linkedin = request.POST.get("linkedin")
            frase = request.POST.get("frase")
            descricao = request.POST.get("descricao")

            perfil = models.Perfil.objects.get(user=request.user)

            perfil.instagram = instagram
            perfil.twitter = twitter
            perfil.github = github
            perfil.tiktok = tiktok
            perfil.linkedin = linkedin
            perfil.frase = frase
            perfil.sobre = descricao

            perfil.save()

            return redirect('userperfil')
        except:
            return HttpResponse("ERRO")

@login_required(login_url='account/logar')        
def add_projeto(request):

    nome = request.POST.get('nome')
    link = request.POST.get('link')
    print(nome, link)

    perfil = models.Perfil.objects.get(user=request.user)
    
    if perfil.lenProjects < 10:
        projeto = models.UsersProjects.objects.create(
            nome = nome,
            link = link,
            user = request.user,
        )
        projeto.save()
        perfil.lenProjects += 1
        perfil.save()
    else:
        print("LIMITE DE PROJETO ATINGIDO")
        return redirect("userperfil")
    return redirect("userperfil")

@login_required(login_url='account/logar')        
def remover_projeto(request, id):
    projeto = models.UsersProjects.objects.get(id=id)
    perfil = models.Perfil.objects.get(user=request.user)
    if not projeto.user == request.user:
        return redirect('userperfil')
    
    projeto.delete()
    if perfil.lenProjects > 0:
        perfil.lenProjects -= 1
        perfil.save()
    return redirect('userperfil')
    