# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-03-21 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0006_animals'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='animals',
            managers=[
                ('a_m', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='animals',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]