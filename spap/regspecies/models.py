from __future__ import unicode_literals
from django.db import models

# Create your models here.

# Plantae Registered
class RegPlantae(models.Model):
	regplantaeassam = models.AutoField(primary_key=True,db_index=True)
	plantae = models.ForeignKey('speciesdata.Plantae')
	images = models.ForeignKey('media.PlantaeImages')
	beat = models.ForeignKey('departments.Beat')
	islive = models.BinaryField(default=True)
	state = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	# Replace it with some Geo Django model fields
	latitude = models.DecimalField(max_digits=9, decimal_places=2)
	longitude = models.DecimalField(max_digits=9, decimal_places=2)
	data1 = models.CharField(max_length=20,null=True)
	data2 = models.CharField(max_length=20,null=True)


'''
Simillarly we can have tables for different Kingdom(Taxonomy)
'''