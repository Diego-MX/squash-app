# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20180322_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player2',
            field=models.TextField(default='Player2'),
        ),
    ]
