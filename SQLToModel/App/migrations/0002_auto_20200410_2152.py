# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-04-10 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_icon',
            field=models.ImageField(upload_to='%Y/%m/%d/icons'),
        ),
    ]
