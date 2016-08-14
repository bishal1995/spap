from __future__ import unicode_literals
from django.contrib.gis.db import models

# Create your models here.

class PlantaeImages(models.Model):
	images = models.AutoField(primary_key=True,db_index=True)
	thumbnail = models.ImageField(upload_to='images/',null=True)
	image1 = models.ImageField(upload_to='images/',null=True)
	image2 = models.ImageField(upload_to='images/',null=True)
