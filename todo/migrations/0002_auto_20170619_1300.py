# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='date_completed',
            field=models.DateTimeField(blank=True, verbose_name='Date completed'),
        ),
    ]
