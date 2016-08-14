from __future__ import unicode_literals
from django.contrib.gis.db import models

# AreaType
ATY = (
	('BT','Beat'),
	('RN','Range'),
	('DI','Division'),
	('IG','Indegenous Patch'),
)

class gisArea(models.Model):
	gisarea = models.AutoField(primary_key=True,db_index=True)
	areaType = models.CharField(max_length=2,choices=ATY,null=True)
	boundry = models.PolygonField(null=True)


