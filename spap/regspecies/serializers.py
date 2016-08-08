from rest_framework import serializers
from .models import RegPlantae

class RegPlantaeSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegPlantae
		fields = ('regplantae','plantae','images','beat','state','district','latitude','longitude','ptype','data2')

class RegPlantaeListSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegPlantae
		fields = ('regplantae','images','ptype')
		