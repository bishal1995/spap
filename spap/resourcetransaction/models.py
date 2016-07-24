from __future__ import unicode_literals
from django.db import models

# Create your models here.
#1) Transaction choices - can augument later if needed
TRT = (
	('CO','Collection'),
	('DS','Distribution'),
)
#2) Transaction from group- can augument later if needed
TFB = (
	('DI','Division'),
	('RN','Range'),
	('BT','Beat'),
)
#3) Transaction to group- can augument later if needed
TTB = (
	('DI','Division'),
	('RN','Range'),
	('BT','Beat'),
)
#4) Transaction from officer Type- can augument later if needed
TRO = (
	('DO','Division officer'),
	('RO','Range officer'),
	('BO','Beat officer'),
)
#5) Transaction to officer Type - can augument later if needed
TTO = (
	('DO','Division officer'),
	('RO','Range officer'),
	('BO','Beat officer'),
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
	collfromg = models.CharField(max_length=2,choices=TFB) # group type
	colltog = models.CharField(max_length=2,choices=TTB) # group type
	collfromg_id = models.PositiveIntegerField() # group ID
	colltog_id = models.PositiveIntegerField() # group ID
	collfromU = models.CharField(max_length=2,choices=TRO) # User type
	colltoU = models.CharField(max_length=2,choices=TTO) # User type
	collfromU_id = models.PositiveIntegerField() # User ID
	colltoU_id = models.PositiveIntegerField() # User ID
	plant = models.ForeignKey('') # registered plant
	coll_amount = models.PositiveSmallIntegerField()
	date = models.DateField(auto_now_add=False)
	time = models.TimeField(auto_now_add=False)

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
	plant = models.ForeignKey('')    # registered plant
	dis_amount = models.PositiveSmallIntegerField()
	date = models.DateField(auto_now_add=False)
	time = models.TimeField(auto_now_add=False)

# Simillarly we can augument the many type of transaction for many type of resources

# Transactions to be dove after updating the collection,distribution and balance
class Transaction(models.Model):
	seedtransaction =  models.AutoField(primary_key=True,db_index=True)
	trantype = models.CharField(max_length=2,choices=TRT) # Transaction Type
	tran_id = models.IntField() # either a collection or distribution ID
	trangood = models.CharField(max_length=2,choices=TRG) # Transaction good
	regbeing_type = models.CharField(max_length=2,choices=RBT)
	regbeing_id = models.ForeignKey('')  # registered species
	tranfromg = models.CharField(max_length=2,choices=TFB) # group type
	trantog = models.CharField(max_length=2,choices=TTB) # group type
	tranfromg_id = models.PositiveIntegerField() # group ID
	trantog_id = models.PositiveIntegerField() # group ID
	tranfromU = models.CharField(max_length=2,choices=TRO) # User type
	trantoU = models.CharField(max_length=2,choices=TTO) # User type
	tranfromU_id = models.PositiveIntegerField() # User ID
	trantoU_id = models.PositiveIntegerField() # User ID
	transaction_amount = models.PositiveSmallIntegerField()
	bal_dec_from = models.ForeignKey('')
	bal_add_to = models.ForeignKey('')
	date = models.DateField(auto_now_add=False)
	time = models.TimeField(auto_now_add=False)


'''
Reasons for different collection and distribution tables is viewing permission

'''

































































