from __future__ import unicode_literals
from speciesdata.models import Plantae
from django.contrib.gis.db import models

# Create your models here.
#6) Deposited goods - can augument later if needed
RST = (
	('SD','Seed'),
)
#7) Deposited being type - can augument later if needed
RBT = (
	('PL','Plant'),
)
#3) Deposited body type - can augument later if needed
DBT = (
	('DI','Division'),
	('RN','Range'),
	('BT','Beat'),
)

class SeedDeposit(models.Model):
	account = models.AutoField(primary_key=True,db_index=True)
	body_type = models.CharField(max_length=2,choices=DBT) # Owner type
	body_id = models.PositiveIntegerField()				   # Owner ID
	source_species = models.ForeignKey(Plantae,null=True)
	balance = models.PositiveIntegerField()
	open_date = models.DateField(auto_now_add=True)
	open_time = models.TimeField(auto_now_add=True)
	last_updated_date = models.DateField(auto_now=True)
	last_updated_time = models.TimeField(auto_now=True)
	#status = models.BinaryField(default=True) # reveals is it operatable or not
	def __unicode__(self):
		return str(self.body_id)

class ResourceDeposit(models.Model):
	account = models.AutoField(primary_key=True,db_index=True)
	body_type = models.CharField(max_length=2,choices=DBT) # Owner type
	body_id = models.PositiveIntegerField()				   # Owner ID
	resource_type = models.CharField(max_length=2,choices=RST)
	resource_bank_id = models.PositiveIntegerField()
	source_species = models.PositiveIntegerField()
	balance = models.DecimalField(max_digits=9, decimal_places=2)
	open_date = models.DateField(auto_now_add=True)
	open_time = models.TimeField(auto_now_add=True)
	last_updated_date = models.DateField(auto_now=True)
	last_updated_time = models.TimeField(auto_now=True)
	status = models.BinaryField(default=True) # reveals is it operatable or not


