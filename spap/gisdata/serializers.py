from rest_framework import serializers
from .models import gisArea,cordinates

class gisAreaSerializer(serializers.ModelSerializer):
	class Meta:
		model = gisArea
		fields = ('gisArea')

class cordinatesSerializer(serializers.ModelSerializer):
	class Meta:
		models = cordinates
		fields = ('area','latitude','longitude')
