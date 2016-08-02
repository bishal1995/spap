from rest_framework import serializers
from .models import Plantae,PlantaeHindi,PlantaeAssamese,PlantaeBengali

class PlantaeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Plantae
		fields = (
				'plantae', 
				'scientific_name', 
				'local_name', 
				'apd', 
				'canopy_height', 
				'Phylum', 
				'Class', 
				'Series', 
				'Family', 
				'Genus',
				'Species', 
				'distribution', 
				'evapotranspiration',
				'leaf_dissection', 
				'leaf_margin', 
				'leaf_size', 
				'life_form',
				'lifespan', 
				'main_axis_diameter', 
				'phenology',
				'pollen_aggregation', 
				'pollen_size', 
				'pollen_surface',
				'pollen_vector', 
				'seed_dispersal',
				'seeds_diaspore', 
				'seed_size_class',
				'sporophyte_cost',
				'status',
				)

class PlantaeHindiSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlantaeHindi
		fields = ('plantae','scientific_name','local_name','comments')

class PlantaeAssameseSerializer(serializers.ModelSerializer):
	class Model:
		model = PlantaeAssamese
		fields = ('plantae','scientific_name','local_name','comments')

class PlantaeBengaliSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlantaeBengali
		fields = ('plantae','scientific_name','local_name','comments')












































