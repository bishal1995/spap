from __future__ import unicode_literals

from django.db import models

# Create your models here.

class gisArea(models.Model):
	gisarea = models.AutoField(primary_key=True,db_index=True)


class cordinates(models.Model):
	area = models.OneToOneField(gisArea,primary_key=True,db_index=True)
	latitude = models.DecimalField(max_digits=9, decimal_places=2)
	longitude = models.DecimalField(max_digits=9, decimal_places=2)




