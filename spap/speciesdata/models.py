from __future__ import unicode_literals
from django.db import models
# Create your models here.

#Options
#1) Anti-Predation Devices

APD = (
	('invt','anti-invertebrate defenses'),
	('vert','anti-vertebrate defenses'),
	('v/it','both kinds of defenses'),
	('none','no defence'),
)
#2) Distribution
DST = (
	('CL','clumped'),
	('DI','dispersed'),
)
#3) Evapotranspiration
EVT = (
	('DM','dimorph_meso-hygro'),
	('DX','dimorph_xero-meso'),
	('HY','hygromorphic'),
	('ME','mesomorphic'),
	('XE','xeromorphic'),
)
#4) Leaf Disection
LDS = (
	('PA','palmately_cmpd'),
	('PI','pinnately_cmpd'),
	('PT','pinnatifid'),
	('SI','simple'),
	('SP','simple_palmate'),
	('SE','simple_pinnate'),
)
#5) Leaf Margin
LMR = (
	('DT','drip_tip'),
	('ET','entire'),
	('LB','lobed'),
	('LT','lobed+th'),
	('TO','toothed'),
)
#6) Leaf Size
LFZ = (
	('MA','macrophyll'),
	('ME','megaphyll'),
	('MS','mesophyll'),
	('MI','microphyll'),
	('NA','nanophyll'),
	('NO','notophyll'),
)
#7) Life form
LFR = (
	('01','cespitose'),
	('02','decumbent'),
	('03','emerg_aquat'),
	('04','epiphyte'),
	('05','float_aqu'),
	('06','ground_cover'),
	('07','herb'),
	('08','herb_liana'),
	('09','parasite'),
	('10','perenn_herb'),
	('11','procumbent'),
	('12','prostrate'),
	('13','semi_self_su'),
	('14','shrub'),
	('15','small_tree'),
	('16','tree'),
	('17','woody_liana'),
)
#8) Lifespan
LSF = (
	('AN','annual'),
	('LP','long_liv_perennial'),
	('MC','monocarpic'),
	('SL','short_liv_perennia')
)
#9) Phenology
PHL = (
	('DE','deciduous'),
	('EV','evergreen'),
)
#10) Pollen Aggregation
PAG = (
	('MO','monad'),
	('OT','other'),
)
#11) Pollen Surface
PSF = (
	('SC','sculptured'),
	('SM','smooth'),
)
#12) Pollen Vector
PVR = (
	('AN','animal'),
	('WA','water'),
	('WN','wind'),
)
#13 Seed Dispersal
SDR = (
	('EA','endo-animal'),
	('EX','exo-animal'),
	('NO','none'),
	('WA','water'),
	('WI','wind'),
)
#14) sporophyte_cost
SPC = (
	('KP','K+'),
	('KM','K-'),
	('RP','r+'),
	('RM','r-'),
	('RK','r-K'),
	('UN','unknown'),
)
# Main species data - In English
class Plantae(models.Model):
	plant = models.AutoField(primary_key=True,db_index=True)
	scientific_name = models.CharField(max_length=40)
	local_name = models.CharField(max_length=40)
	apd = models.CharField(max_length=4,choices=APD)
	canopy_height = models.PositiveSmallIntegerField()
	Phylum = models.CharField(max_length=30)
	Class = models.CharField(max_length=30)
	Series = models.CharField(max_length=30)
	Family = models.CharField(max_length=30)
	Genus = models.CharField(max_length=30)
	Species = models.CharField(max_length=30)
	clonal_growth = models.NullBooleanField()
	distribution = models.CharField(max_length=2,choices=DST)
	evapotranspiration = models.CharField(max_length=2,choices=EVT)
	leaf_dissection = models.CharField(max_length=2,choices=LDS)
	leaf_margin = models.CharField(max_length=2,choices=LMR)
	leaf_size = models.CharField(max_length=2,choices=LFZ)
	life_form = models.CharField(max_length=2,choices=LFR)
	lifespan = models.CharField(max_length=2,choices=LSF)
	main_axis_diameter = models.DecimalField(max_digits=7, decimal_places=2)
	phenology = models.CharField(max_length=2,choices=PHL)
	pollen_aggregation = models.CharField(max_length=2,choices=PAG)
	pollen_size = models.DecimalField(max_digits=7, decimal_places=2)
	pollen_surface = models.CharField(max_length=2,choices=PSF)
	pollen_vector = models.CharField(max_length=2,choices=PVR)
	predation = models.BinaryField()
	seed_dispersal = models.CharField(max_length=2,choices=SDR)
	seeds_diaspore models.PositiveSmallIntegerField()
	seed_size_class = models.PositiveSmallIntegerField()
	sporophyte_cost = models.CharField(max_length=2,choices=SPC)
	status = models.BinaryField()
# Species Data - In Hindi
class PlantaeHindi(models.Model):
	plant = models.ForeignKey(Plantae)
	scientific_name = models.CharField(max_length=40)
	local_name = models.CharField(max_length=40)
	comments = models.TextField(max_length=300)	
# Species data - In Assamese 
class PlantaeAssamese(models.Model):
	plant = models.ForeignKey(Plantae)
	scientific_name = models.CharField(max_length=40)
	local_name = models.CharField(max_length=40)
	comments = models.TextField(max_length=300)	
# Species data - In Bengali
class PlantaeBengali(models.Model):
	plant = models.ForeignKey(Plantae)
	scientific_name = models.CharField(max_length=40)
	local_name = models.CharField(max_length=40)
	comments = models.TextField(max_length=300)	

'''
Later Use Signals / Celery to update all models .

Simmilarly we can have several models for all languages, hence making this model 
fully sustainable in a multi lingual county India

Transllations are provided locally in App for fields which have choices or boolean or number



'''