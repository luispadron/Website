# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
