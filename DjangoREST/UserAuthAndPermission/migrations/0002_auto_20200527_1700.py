# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-05-27 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthAndPermission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
