# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-23 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20170523_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
