# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-06 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_caption',
            field=models.CharField(max_length=61),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(max_length=61),
        ),
    ]
