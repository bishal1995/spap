from __future__ import unicode_literals
from django.contrib.gis.db import models

# Create your models here.
#1) Transaction choices - can augument later if needed
TRT = (
	('CO','Collection'),
	('DS','Distribution'),
	('SC','Species_Collection'),
	('GC','Distributed_body'),
)
#2) Transaction from group- can augument later if needed
TFB = (
	('DI','Division'),
	('RN','Range'),
	('BT','Beat'),
	('BC','Beat_collection'),
)
#3) Transaction to group- can augument later if needed
TTB = (
	('DI','Division'),
	('RN','Range'),
	('BT','Beat'),
	('DD','Division_distribution'),
)
#4) Transaction from officer Type- can augument later if needed
TRO = (
	('DO','Division officer'),
	('RO','Range officer'),
	('BO','Beat officer'),
	('RS','RegSpecies'),
)
#5) Transaction to officer Type - can augument later if needed
TTO = (
	('DO','Division officer'),
	('RO','Range officer'),
	('BO','Beat officer'),
	('CC','Government_customer'),
)
#6) Transaction goods - can augument later if needed
TRG = (
	('SD','Seed'),
)
#7) Registered being type - can augument later if needed
RBT = (
	('PL','Plant'),
)

# Seed collections
class SeedCollection(models.Model):
	seedcollection = models.AutoField(primary_key=True,db_index=True)
	collfromg = models.CharField(max_length=2,choices=TFB,default='BC') # group type
	colltog = models.CharField(max_length=2,choices=TTB,default='BT') # group type
	collfromg_id = models.PositiveIntegerField(default=0) # group ID
	colltog_id = models.PositiveIntegerField() # group ID
	collfromU = models.CharField(max_length=2,choices=TRO,default='RS') # User type
	colltoU = models.CharField(max_length=2,choices=TTO,default='BO') # User type
	collfromU_id = models.PositiveIntegerField(default=0) # User ID
	colltoU_id = models.PositiveIntegerField() # User ID
	plant = models.ForeignKey('regspecies.RegPlantae') # registered plant
	coll_amount = models.PositiveSmallIntegerField()
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)

# Seed Distributions
class SeedDistribution(models.Model):
	seeddistribution = models.AutoField(primary_key=True,db_index=True)
	disfromg = models.CharField(max_length=2,choices=TFB) # group type
	distog = models.CharField(max_length=2,choices=TTB) # group type
	disfromg_id = models.PositiveIntegerField() # group ID
	distog_id = models.PositiveIntegerField() # group ID
	disfromU = models.CharField(max_length=2,choices=TRO) # User type
	distoU = models.CharField(max_length=2,choices=TTO) # User type
	disfromU_id = models.PositiveIntegerField() # User ID
	distoU_id = models.PositiveIntegerField() # User ID
	plant = models.ForeignKey('regspecies.RegPlantae')    # registered plant
	dis_amount = models.PositiveSmallIntegerField()
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)

# Simillarly we can augument the many type of transaction for many type of resources

# Transactions to be dove after updating the collection,distribution and balance
class Transaction(models.Model):
	transaction =  models.AutoField(primary_key=True,db_index=True)
	trantype = models.CharField(max_length=2,choices=TRT) # Transaction Type
	tran_id = models.PositiveIntegerField() # either a collection or distribution ID
	trangood = models.CharField(max_length=2,choices=TRG) # Transaction good
	regbeing_type = models.CharField(max_length=2,choices=RBT)
	regbeing_id = models.PositiveIntegerField()  # registered species
	tranfromg = models.CharField(max_length=2,choices=TFB) # group type
	trantog = models.CharField(max_length=2,choices=TTB) # group type
	tranfromg_id = models.PositiveIntegerField() # group ID
	trantog_id = models.PositiveIntegerField() # group ID
	tranfromU = models.CharField(max_length=2,choices=TRO) # User type
	trantoU = models.CharField(max_length=2,choices=TTO) # User type
	tranfromU_id = models.PositiveIntegerField() # User ID
	trantoU_id = models.PositiveIntegerField() # User ID
	transaction_amount = models.PositiveSmallIntegerField()
	bal_dec_from = models.ForeignKey('resourcebank.ResourceDeposit',related_name='from+')
	bal_add_to = models.ForeignKey('resourcebank.ResourceDeposit',related_name='to+')
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)

'''
Reasons for different collection and distribution tables is viewing permission

'''