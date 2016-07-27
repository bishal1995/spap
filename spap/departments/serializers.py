from rest_framework import serializers
from .models import Division,Range,Beat

class DivisionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Division
		fields = ('division','state','district','division_name','gisArea')

class RangeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Range
		fields = ( 'ranges','state','district','range_name','division','gisArea' )

class BeatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Beat
		fields = ( 'beat','state','district','beat_name','ranges','division','gisArea' )