# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='price',
            field=models.IntegerField(default=5000, verbose_name='\u4ef7\u683c'),
        ),
    ]
