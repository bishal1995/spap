from __future__ import unicode_literals
from django.db import models

# Create your models here.

# Plantae Registered
class RegPlantae(models.Model):
	regplantaeassam = models.AutoField(primary_key=True,db_index=True)
	plantae = models.ForeignKey('')
	images = models.ForeignKey('')
	beat = models.ForeignKey('')
	islive = models.BinaryField(default=True)
	state = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	# Replace it with some Geo Django model fields
	latitude = models.DecimalField(max_digits=None, decimal_places=None, attributes)
	longitude = models.DecimalField(max_digits=None, decimal_places=None, attributes)
	data1 = models.CharField(max_length=20)
	data2 = models.CharField(max_length=20)
	data3 = models.CharField(max_length=20)
	data4 = models.CharField(max_length=20)
	data5 = models.CharField(max_length=20)



'''
Simillarly we can have tables for different Kingdom(Taxonomy)
'''