# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-28 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='average',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='design',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='usability',
            field=models.IntegerField(default=0),
        ),
    ]