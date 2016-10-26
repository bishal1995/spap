from __future__ import unicode_literals
from django.contrib.gis.db import models


class Division(models.Model):
    division = models.AutoField(primary_key=True,db_index=True)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    division_name = models.CharField(max_length=40)
    gisArea = models.ForeignKey('gisdata.gisArea',null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6,null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6,null=True)
    def __unicode__(self):
        return str(str(self.division)+" "+self.division_name)

class Range(models.Model):
    ranges = models.AutoField(primary_key=True,db_index=True)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    range_name = models.CharField(max_length=30)
    division = models.ForeignKey(Division)
    gisArea = models.ForeignKey('gisdata.gisArea',null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6,null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6,null=True)
    def __unicode__(self):
        return str(str(self.ranges)+" "+self.range_name)
 
class Beat(models.Model):
    beat = models.AutoField(primary_key=True,db_index=True)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    beat_name = models.CharField(max_length=30)
    ranges = models.ForeignKey(Range)
    division = models.ForeignKey(Division)
    gisArea = models.ForeignKey('gisdata.gisArea',null=True) # from gis data
    latitude = models.DecimalField(max_digits=8, decimal_places=6,null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6,null=True)
    def __unicode__(self):
        return str(str(self.beat)+' '+self.beat_name)    
