# Generated by Django 4.2.4 on 2023-09-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0003_perfil_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='portfolio',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
