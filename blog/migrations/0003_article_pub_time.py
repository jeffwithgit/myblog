# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-11 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180209_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.TimeField(auto_now=True),
        ),
    ]