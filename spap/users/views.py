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

from .models import DivisionOfficer,RangeOfficer,BeatOfficer
from departments.models import  Division,Range,Beat
# Create your views here.
class OfficerInfo(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	throttle_classes = (UserRateThrottle,)

	def get(self,request):
		found = False
		try:
			user = BeatOfficer.objects.get(user=request.user)
			user_details = {}
			user_details['id'] = user.beatofficer
			user_details['off_type'] = 'BO'
			user_details['off_id'] = user.officialID
			user_details['first_name'] = request.user.first_name
			user_details['last_name'] = request.user.last_name
			user_details['division_id'] = user.division.pk
			user_details['division'] = user.division.division_name
			user_details['range_id'] = user.ranged.pk
			user_details['range'] = user.ranged.range_name
			user_details['beat_id'] = user.beat.pk
			user_details['beat'] = user.beat.beat_name
			found = True
			return Response(user_details,status=status.HTTP_200_OK)

		except BeatOfficer.DoesNotExist:
			foo = 1

		try:
			user = RangeOfficer.objects.get(user=request.user)
			user_details = {}
			user_details['id'] = user.rangeofficer
			user_details['off_type'] = 'RO'
			user_details['off_id'] = user.officialID
			user_details['first_name'] = request.user.first_name
			user_details['last_name'] = request.user.last_name
			user_details['division_id'] = user.division.pk
			user_details['division'] = user.division.division_name
			user_details['range_id'] = user.ranged.pk
			user_details['range'] = user.ranged.range_name
			found = True
			return Response(user_details,status=status.HTTP_200_OK)

		except RangeOfficer.DoesNotExist:
			foo = 1

		try:
			user = DivisionOfficer.objects.get(user=request.user)
			user_details = {}
			user_details['id'] = user.divisionofficer
			user_details['off_type'] = 'DO'
			user_details['off_id'] = user.officialID
			user_details['first_name'] = request.user.first_name
			user_details['last_name'] = request.user.last_name
			user_details['division_id'] = user.division.pk
			user_details['division'] = user.division.division_name
			found = True
			return Response(user_details,status=status.HTTP_200_OK)

		except DivisionOfficer.DoesNotExist:
			foo = 1
		if (found==False):
			error = {'error':'Invalid ID'}
			return Response(error,status=status.HTTP_400_BAD_REQUEST)
		else:
			foo = 1



	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(OfficerInfo,self).dispatch(*args, **kwargs)

