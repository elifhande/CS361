# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elifapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='imdb',
            field=models.CharField(default='', max_length=5),
        ),
    ]
