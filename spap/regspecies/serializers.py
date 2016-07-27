from rest_framework import serializers
from .models import RegPlantae

class RegPlantaeSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegPlantae
		fields = ('regplantae','plantae','images','beat','state','district','latitude','longitude','data1','data2')
		