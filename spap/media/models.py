from __future__ import unicode_literals
from django.db import models

# Create your models here.

class PlanteaImages(models.Model):
	images = models.AutoField(primary_key=True,db_index=True)
	propic = models.ImageField(upload_to=None, max_length=100, height_field=None, width_field=None, attributes)
	thumbnail = models.ImageField(upload_to=None, max_length=100, height_field=None, width_field=None, attributes)
	pic1 = models.ImageField(upload_to=None, max_length=100, height_field=None, width_field=None, attributes)
	pic2 = models.ImageField(upload_to=None, max_length=100, height_field=None, width_field=None, attributes)
	pic3 = models.ImageField(upload_to=None, max_length=100, height_field=None, width_field=None, attributes)
	pic4 = models.ImageField(upload_to=None, max_length=100, height_field=None, width_field=None, attributes)

