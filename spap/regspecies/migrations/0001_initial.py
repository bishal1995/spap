# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-01 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0001_initial'),
        ('departments', '0001_initial'),
        ('speciesdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegPlantae',
            fields=[
                ('regplantae', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=9)),
                ('data1', models.CharField(max_length=20, null=True)),
                ('data2', models.CharField(max_length=20, null=True)),
                ('islive', models.BinaryField(default=True)),
                ('beat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Beat')),
                ('images', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='media.PlantaeImages')),
                ('plantae', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciesdata.Plantae')),
            ],
        ),
    ]
