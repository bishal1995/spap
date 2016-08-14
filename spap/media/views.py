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
from django.core.files.images import ImageFile
import json,decimal

from .models import PlantaeImages

# Image uploader
class ImageUploadAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	throttle_classes = (UserRateThrottle,)

	def put(self,request):
		imgFile = request.FILES['image']
		plImage = PlantaeImages()
		plImage.thumbnail = ImageFile(imgFile)
		plImage.save()
		data = {'image_id': plImage.images }
		return Response(data,status=status.HTTP_200_OK)


	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(ImageUploadAPI,self).dispatch(*args, **kwargs)

