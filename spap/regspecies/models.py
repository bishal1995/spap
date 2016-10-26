from __future__ import unicode_literals
from django.contrib.gis.db import models
from gisdata.models import gisArea
# Create your models here.

## Type of tree 
TY = (
	('SB','Seed Bearing'),
	('IG','Ingeneous tree'),
	('IP','Indegenous patch'),
)

# Plantae Registered
class RegPlantae(models.Model):
	regplantae = models.AutoField(primary_key=True,db_index=True)
	plantae = models.ForeignKey('speciesdata.Plantae')
	images = models.ForeignKey('media.PlantaeImages',null=True)
	beat = models.ForeignKey('departments.Beat')
	state = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	latitude = models.DecimalField(max_digits=9, decimal_places=2)
	longitude = models.DecimalField(max_digits=9, decimal_places=2)
	ptype = models.CharField(max_length=2,choices=TY,null=True)
	patch = models.ForeignKey(gisArea,null=True,blank=True)
	def __unicode__(self):
		return self.plantae.scientific_name

'''
Simillarly we can have tables for different Kingdom(Taxonomy)
'''