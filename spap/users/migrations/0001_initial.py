# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-01 10:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeatOfficer',
            fields=[
                ('beatofficer', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('officialID', models.CharField(max_length=20)),
                ('beat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Beat')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Division')),
                ('ranged', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Range')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DivisionOfficer',
            fields=[
                ('divisionofficer', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('officialID', models.CharField(max_length=20)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Division')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RangeOfficer',
            fields=[
                ('rangeofficer', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('officialID', models.CharField(max_length=20)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Division')),
                ('ranged', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Range')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
