from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.contrib.auth.models import User
# Create your models here.
class DivisionOfficer(models.Model):
	divisionofficer = models.AutoField(primary_key=True,db_index=True)
	user = models.OneToOneField(User)
	officialID = models.CharField(max_length=20)
	division = models.ForeignKey('departments.Division')


class RangeOfficer(models.Model):
	rangeofficer = models.AutoField(primary_key=True,db_index=True)
	user = models.OneToOneField(User)
	officialID = models.CharField(max_length=20)
	division = models.ForeignKey('departments.Division')
	ranged = models.ForeignKey('departments.Range')

class BeatOfficer(models.Model):
	beatofficer = models.AutoField(primary_key=True,db_index=True)
	user = models.OneToOneField(User)
	officialID = models.CharField(max_length=20)
	division = models.ForeignKey('departments.Division')
	ranged = models.ForeignKey('departments.Range')
	beat = models.ForeignKey('departments.Beat')

class LoginInfo(models.Model):
	user = models.OneToOneField(User)
	last_activity = models.DateTimeField(auto_now=False, auto_now_add=False)

'''
Simillarly we can have various officials at various levels inheritting the properties

'''