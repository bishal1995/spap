# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resourcebank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seeddeposit',
            name='status',
        ),
    ]