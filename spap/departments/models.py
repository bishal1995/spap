from __future__ import unicode_literals
from django.db import models


class Division(models.Model):
	division = models.AutoField(primary_key=True,db_index=True)
	state = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	division_name = models.CharField(max_length=40)
	gisArea = models.ForeignKey('gisdata.gisArea',null=True)
	is_active = models.BinaryField(default=True)

class Range(models.Model):
	ranges = models.AutoField(primary_key=True,db_index=True)
	state = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	range_name = models.CharField(max_length=30)
	division = models.ForeignKey(Division)
	gisArea = models.ForeignKey('gisdata.gisArea',null=True)
	is_active = models.BinaryField(default=True)

class Beat(models.Model):
	beat = models.AutoField(primary_key=True,db_index=True)
	state = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	beat_name = models.CharField(max_length=30)
	ranges = models.ForeignKey(Range)
	division = models.ForeignKey(Division)
	gisArea = models.ForeignKey('gisdata.gisArea',null=True) # from gis data
	is_active = models.BinaryField(default=True)

	