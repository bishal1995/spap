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

# Module models
from .models import gisArea,cordinates
from .serializers import gisAreaSerializer,cordinatesSerializer

# Gisdata models CRUD methods

class gisAreaAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	throttle_classes = (UserRateThrottle,)

	def get(self,request):
		area_id = int(request.GET['id'])
		try:
			gisarea = gisArea.objects.get(gisarea=area_id)
			serializer = gisAreaSerializer(gisarea,many=True)
			return Response(serializer.data,status=status.HTTP_200_OK)
		except gisArea.DoesNotExist:
			error = {'error':'Invalid Area ID'}
			return Response(error,status=status.HTTP_400_BAD_REQUEST)

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(gisAreaAPI,self).dispatch(*args, **kwargs)

class cordinatesAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	throttle_classes = (UserRateThrottle,)

	def get(self,request):
		area_id = int(request.GET['id'])
		try:
			gisarea = gisArea.objects.get(gisarea=area_id)
			cordinate = cordinates.objects.filter(area=gisarea)
			serializer = cordinatesSerializer(cordinate,many=True)
			return Response(serializer.data,status=status.HTTP_200_OK)

		except gisArea.DoesNotExist:
			error = {'error':'Invalid Area Id'}
			return Response(error,status=status.HTTP_400_BAD_REQUEST)

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(cordinatesAPI,self).dispatch(*args, **kwargs)






























































