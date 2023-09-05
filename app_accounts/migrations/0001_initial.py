# Generated by Django 4.2.4 on 2023-08-21 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersprojects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.CharField(default=None, max_length=50)),
                ('instagram', models.CharField(default='brenndoncj', max_length=50)),
                ('twitter', models.CharField(default=None, max_length=50)),
                ('linkedin', models.CharField(default=None, max_length=50)),
                ('tiktok', models.CharField(default=None, max_length=50)),
                ('frase', models.CharField(default=None, max_length=144)),
                ('sobre', models.TextField(default=None)),
                ('img_background', models.URLField()),
                ('img_sobre', models.URLField()),
                ('lenProjects', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userperfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]