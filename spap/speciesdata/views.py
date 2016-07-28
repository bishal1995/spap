from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json,decimal

# module packages
from .serializers import PlantaeSerializer,PlantaeHindiSerializer,PlantaeAssameseSerializer,PlantaeBengaliSerializer
from .models import Plantae,PlantaeHindi,PlantaeAssamese,PlantaeBengali

class PlantaeAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	throttle_classes = (UserRateThrottle,)

	def get(self,request):
		plantae_id = int(request.GET['id'])
		try:
			plantae = Plantae.objects.get(plantae=plantae_id)
			serializer = PlantaeSerializer(plantae)
			return Response(serializer.data,status=status.HTTP_200_OK)

		except Plantae.DoesNotExist:
			error = {'error':'InvalidPlantae ID'}
			return Response(error,status=status.HTTP_400_BAD_REQUEST)

	def put(self,request):
		plantae_reg = request.data
		plantae_reg = json.loads(plantae_reg)
		plantae = Plantae()
		plantae['scientific_name'] = plantae_reg['scientific_name']
		plantae['local_name'] = plantae_reg['local_name']
		plantae['apd'] = plantae_reg['apd']
		plantae['canopy_height'] = plantae_reg['canopy_height']
		plantae['Phylum'] = plantae_reg['Phylum']
		plantae['Class'] = plantae_reg['Class']
		plantae['Series'] = plantae_reg['Series']
		plantae['Family'] = plantae_reg['Family']
		plantae['Genus'] = plantae_reg['Genus']
		plantae['Species'] = plantae_reg['Species']
		plantae['clonal_growth'] = plantae_reg['clonal_growth']
		plantae['distribution'] = plantae_reg['distribution']
		plantae['evapotranspiration'] = plantae_reg['evapotranspiration']
		plantae['leaf_dissection'] = plantae_reg['leaf_dissection']
		plantae['leaf_margin'] = plantae_reg['leaf_margin']
		plantae['leaf_size'] = plantae_reg['leaf_size']
		plantae['life_form'] = plantae_reg['life_form']
		plantae['lifespan'] = plantae_reg['lifespan'] 
		plantae['main_axis_diameter'] = plantae_reg['main_axis_diameter']
		plantae['phenology'] = plantae_reg['phenology']
		plantae['pollen_aggregation'] = plantae_reg['pollen_aggregation']
		plantae['pollen_size'] = plantae_reg['pollen_size']
		plantae['pollen_surface'] = plantae_reg['pollen_surface']
		plantae['pollen_vector'] = plantae_reg['pollen_vector']
		plantae['predation'] = plantae_reg['predation']
		plantae['seed_dispersal'] = plantae_reg['seed_dispersal']
		plantae['seeds_diaspore'] = plantae_reg['seeds_diaspore']
		plantae['seed_size_class'] = plantae_reg['seed_size_class']
		plantae['sporophyte_cost'] = plantae_reg['sporophyte_cost']
		plantae['status'] = plantae_reg['status']
		plantae.save()
		data = {'plantae':plantae.plantae_reg}
		return Response(data,status=status.HTTP_200_OK)

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(PlantaeAPI,self).dispatch(*args, **kwargs)









