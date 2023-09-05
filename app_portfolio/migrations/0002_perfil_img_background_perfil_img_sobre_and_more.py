# Generated by Django 4.2.4 on 2023-08-18 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='img_background',
            field=models.URLField(default=datetime.datetime(2023, 8, 18, 22, 16, 21, 766946, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='img_sobre',
            field=models.URLField(default=datetime.datetime(2023, 8, 18, 22, 16, 29, 573962, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='instagram',
            field=models.CharField(default='brenndoncj', max_length=50),
        ),
    ]
