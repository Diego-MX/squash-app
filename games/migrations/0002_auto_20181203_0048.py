# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-03 00:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('id',)},
        ),
    ]