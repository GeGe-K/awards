# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-23 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='projects',
        ),
    ]
