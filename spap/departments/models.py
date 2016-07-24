from __future__ import unicode_literals
from django.db import models


class Division(models.Model):
	division = models.AutoField(primary_key=True,db_index=True)
	state = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	division_name = models.CharField(max_length=40)
	gisArea = models.ForeignKey('')

class Range(models.Model):
	ranges = models.AutoField(primary_key=True,db_index=True)
	state = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	rangename = models.CharField(max_length=30)
	division = models.ForeignKey(Division)
	gisArea = models.ForeignKey('')

class Beat(models.Model):
	best = models.AutoField(primary_key=True,db_index=True)
	state = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	beatname = models.CharField(max_length=30)
	ranges = models.ForeignKey(Range)
	division = models.ForeignKey(Division)
	gisArea = models.ForeignKey('') # from gis data

	