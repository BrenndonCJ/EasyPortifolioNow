from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    __tablename__ = "perfil"

    github = models.CharField(max_length=50, default=None, null=True)
    instagram = models.CharField(max_length=50, null=True)
    twitter = models.CharField(max_length=50, default=None, null=True)
    linkedin = models.CharField(max_length=50, default=None, null=True)
    tiktok = models.CharField(max_length=50, default=None, null=True)
    frase = models.CharField(max_length=144, default=None, null=True)
    sobre = models.TextField(default=None, null=True)

    img_background = models.URLField(null=True)
    img_sobre = models.URLField(null=True)

    portfolio = models.CharField(max_length=250 ,null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userperfil")
    lenProjects = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username

class UsersProjects(models.Model):
    """
    Tabela de URLs no banco de dados

    ...

    Atributos
    ----------
    nome : str
        ...
    url : str
        ...
    user : User
        ...
    """
    __tablename__ = "usersprojects"

    nome:str = models.CharField(max_length=50)
    link:models.CharField = models.CharField(max_length=150)
    user:User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usersprojects")

    def __str__(self) -> str:
        return self.nome