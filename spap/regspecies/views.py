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
from django.contrib.gis.geos import GEOSGeometry,Point,Polygon
import json,decimal,ast

# Module models
from .models import RegPlantae
from speciesdata.models import Plantae
from media.models import PlantaeImages
from departments.models import Beat
from .serializers import RegPlantaeSerializer,RegPlantaeListSerializer
from gisdata.models import gisArea

class RegPlantaeAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	throttle_classes = (UserRateThrottle,)

	def get(self,request):
		regplantae_id = int(request.GET['id'])
		try:
			regPlantae = RegPlantae.objects.get(regplantae=regplantae_id)
			serializer = RegPlantaeSerializer(regplantae)
			return Response(serializer.data,status=status.HTTP_200_OK)
		except RegPlantae.DoesNotExist :
			error = {'error':'Invalid Reg-Plantae Id'}
			return Response(error,status=status.HTTP_400_BAD_REQUEST)

	def put(self,request):
		regplantae_data = request.body
		regplantae_data = regplantae_data.replace('\"','"')
		regplantae_data = regplantae_data.replace("\n","")
		regplantae_data = json.loads(regplantae_data)
		plantae_id = int(regplantae_data['plantae'])
		images_id = int(regplantae_data['images'])
		beat_id = int(regplantae_data['beat'])
		if (regplantae_data['ptype'] == 'IG'):
			boundry = ast.literal_eval(regplantae_data['patch'])
			print(type(boundry))
			if ( len(boundry) != 0 ):
				clist = []
				for cordinates in boundry:
					clist.append(GEOSGeometry('POINT(%s %s)'%(cordinates[0],cordinates[1])))
				poly = Polygon(clist)
				area = gisArea()
				area.areaType = 'IG'
				area.boundry = poly
				area.save()
			else : 
				area = None			
		else:
			area = None
		try:
			plantae = Plantae.objects.get(plantae=plantae_id)
			try:
				images = PlantaeImages.objects.get(images=images_id)
				try:
					beat = Beat.objects.get(beat=beat_id)
					regplantae = RegPlantae()
					regplantae.plantae = plantae
					regplantae.images = images
					regplantae.beat = beat
					regplantae.state = regplantae_data['state'] 
					regplantae.district = regplantae_data['district']
					regplantae.latitude = float(regplantae_data['latitude'])
					regplantae.longitude = float(regplantae_data['longitude'])
					regplantae.ptype = regplantae_data['ptype']
					regplantae.patch = area
					regplantae.save()
					data = {'reg_plantae' : regplantae.regplantae }
					return Response(data,status=status.HTTP_200_OK)

				except Beat.DoesNotExist:
					error = {'error':'Invalid Beat Id'}
					return Response(error,status=status.HTTP_400_BAD_REQUEST)
			except PlantaeImages.DoesNotExist :
				error = {'error':'Images Not found'}
				return Response(error,status=status.HTTP_400_BAD_REQUEST)
		except Plantae.DoesNotExist:
			error = {'error':'Invalid Plantae Id'}
			return Response(error,status=status.HTTP_400_BAD_REQUEST)

	def patch(self,request):
		regplantae_data = request.body
		regplantae_data = json.loads(regplantae_data)
		regplantae_id = int(regplantae_data['regplantae'])
		plantae_id = int(regplantae_data['plantae'])
		images_id = int(regplantae_data['images'])
		beat_id = int(regplantae_data['beat'])
		if (regplantae_data['ptype'] == 'IG'):
			boundry = ast.literal_eval(regplantae_data['patch'])
			print(type(boundry))
			if ( len(boundry) != 0 ):
				clist = []
				for cordinates in boundry:
					clist.append(GEOSGeometry('POINT(%s %s)'%(cordinates[0],cordinates[1])))
				poly = Polygon(clist)
				area = gisArea()
				area.areaType = 'IG'
				area.boundry = poly
				area.save()
			else : 
				area = None			
		else:
			area = None
		try:
			plantae = Plantae.objects.get(plantae=plantae_id)
			try:
				images = PlantaeImages.objects.get(images=images_id)
				try:
					beat = Beat.objects.get(beat=beat_id)
					try:
						regplantae = RegPlantae.objects.get(regplantae=regplantae_id)
						updateparameters = {}
						updateparameters['plantae'] = plantae
						updateparameters['images'] = images
						updateparameters['beat'] = beat
						updateparameters['state'] = regplantae_data['state']
						updateparameters['district'] = regplantae_data['district']
						updateparameters['latitude'] = float(regplantae_data['latitude'])
						updateparameters['longitude'] = float(regplantae_data['longitude'])
						updateparameters['ptype'] = regplantae_data['ptype']
						updateparameters['patch'] = area
						RegPlantae.objects.filter(regplantae=regplantae_id).update(**updateparameters)
						data = {'RegSpecies_updates': regplantae_id }
						return Response(data,status=status.HTTP_200_OK)
					except RegPlantae.DoesNotExist:
						error = {'error':'Invalid Reg-Plantae Id'}
						return Response(error,status=status.HTTP_400_BAD_REQUEST)
				except Beat.DoesNotExist:
					error = {'error':'Invalid Beat Id'}
					return Response(error,status=status.HTTP_400_BAD_REQUEST)
			except PlantaeImages.DoesNotExist :
				error = {'error':'Images Not found'}
				return Response(error,status=status.HTTP_400_BAD_REQUEST)
		except Plantae.DoesNotExist:
			error = {'error':'Invalid Plantae Id'}
			return Response(error,status=status.HTTP_400_BAD_REQUEST)

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(RegPlantaeAPI,self).dispatch(*args, **kwargs)


class RegPlantaeListAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	throttle_classes = (UserRateThrottle,)

	def get(self,request):
		plantaes = RegPlantae.objects.all()
		serializers = RegPlantaeListSerializer(plantaes,many=True)
		return Response(serializers.data,status=status.HTTP_200_OK)

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(RegPlantaeListAPI,self).dispatch(*args, **kwargs)
