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
from .models import Division,Range,Beat
from gisdata.models import gisArea
from .serializers import DivisionSerializer,RangeSerializer,BeatSerializer


# Division model crud methods : 
class DivisionAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    # Get Division Details
    def get(self,request):
        division_id = int(request.GET['id'])
        try:
            division = Division.objects.get(division=division_id)
            serializer = DivisionSerializer(division)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except Division.DoesNotExist:
            error = {'error':'Invalid division ID'}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    # Create A devision
    def put(self,request):
        division_data = request.body
        division_data = json.loads(division_data)
        area_id = int(division_data['gisArea'])
        try:
            gisarea = gisArea.objects.get(gisarea=area_id)
            division = Division()
            division.state = division_data['state']
            division.district = division_data['district']
            division.division_name = division_data['division_name']
            division.gisArea = gisarea
            division.save()
            data = { 'division_id' : division.division }
            return Response(data,status=status.HTTP_200_OK)

        except gisArea.DoesNotExist :
            error = {'error':'Invalid gisArea Id'}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    # Modify a Division
    def patch(self,request):        
        division_data = request.body
        division_data = json.loads(division_data)
        division_id = int(division_data['id'])
        area_id = int(division_data['gisArea'])
        try:
            division = Division.objects.get(division=division_id)
            try:
                gisarea = gisArea.objects.get(gisarea=area_id)
                updateparameters = {}
                updateparameters['state'] = division_data['state']
                updateparameters['district'] = division_data['district']
                updateparameters['division_name'] = division_data['division']
                updateparameters['gisArea'] = gisarea
                Division.objects.filter(division=division_id).update(**updateparameters)
                data = { 'division_updated' : division_id }
                return Response(data,status=status.HTTP_200_OK)
            except gisArea.DoesNotExist :
                error = {'error':'Invalid gisArea Id'}
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
        except Division.DoesNotExist : 
            error = {'error':'Invalid Division ID'}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(DivisionAPI,self).dispatch(*args, **kwargs)

# Range model CRUD methods
class RangeAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    # Get Range Details
    def get(self,request):
        range_id = int(request.GET['id'])
        try:
            ranges = Range.objects.get(ranges=range_id)
            serializer = RangeSerializer(ranges)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except Range.DoesNotExist:
            error = {'error':'Invalid Range ID'}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    # Create A Range
    def put(self,request):
        range_data = request.body
        range_data = json.loads(range_data)
        area_id = int(range_data['gisArea'])
        try:
            gisarea = gisArea.objects.get(gisarea=area_id)
            division_id = int(range_data['division'])
            try:
                division = Division.objects.get(division=division_id)
                ranges = Range()
                ranges.state = range_data['state']
                ranges.district = range_data['district']
                ranges.range_name = range_data['range_name']
                ranges.division = division
                ranges.gisArea = gisarea
                ranges.save()
                data = { 'range_id' : ranges.ranges }
                return Response(data,status=status.HTTP_200_OK)
            except Division.DoesNotExist :
                error = {'error':'Invalid Division ID'}
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
        except gisArea.DoesNotExist :
            error = {'error':'Invalid gisArea Id'}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    # Modify a Range
    def patch(self,request):        
        range_data = request.body
        range_data = json.loads(range_data)
        range_id = int(range_data['id'])
        area_id = int(range_data['gisArea'])
        try:
            ranges = Range.objects.get(ranges=range_id)
            division_id = int(range_data['division'])
            try:
                division = Division.objects.get(division=division_id)
                try:
                    gisarea = gisArea.objects.get(gisarea=area_id)
                    updateparameters = {}
                    updateparameters['state'] = range_data['state']
                    updateparameters['district'] = range_data['district']
                    updateparameters['range_name'] = range_data['range_name']
                    updateparameters['division'] = division
                    updateparameters['gisArea'] = gisarea
                    Range.objects.filter(ranges=range_id).update(**updateparameters)
                    data = { 'range_updated' : range_id }
                    return Response(data,status=status.HTTP_200_OK)
                except gisArea.DoesNotExist :
                    error = {'error':'Invalid gisArea Id'}
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
            except Division.DoesNotExist:
                error = {'error':'Invalid Division Id'}
        except Range.DoesNotExist : 
            error = {'error':'Invalid Range ID'}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(RangeAPI,self).dispatch(*args, **kwargs)

# Beat CRUD methods
# Range model CRUD methods
class BeatAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    # Get Beat Details
    def get(self,request):
        best_id = int(request.GET['id'])
        try:
            beat =  Beat.objects.get(beat=best_id)
            serializer = BeatSerializer(beat)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except Beat.DoesNotExist:
            error = {'error':'Invalid Beat ID'}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    # Create A Beat
    def put(self,request):
        beat_data = request.body
        beat_data = json.loads(beat_data)
        area_id = int(beat_data['gisArea'])
        try:
            gisarea = gisArea.objects.get(gisarea=area_id)
            division_id = int(beat_data['division'])
            try:
                division = Division.objects.get(division=division_id)
                range_id = int(beat_data['ranges'])
                try:
                    ranges = Range.objects.get(ranges=range_id)
                    beat = Beat()
                    beat.state = beat_data['state']
                    beat.district = beat_data['district']
                    beat.beat_name = beat_data['beat_name']
                    beat.ranges = ranges
                    beat.division = division
                    beat.gisArea = gisarea
                    beat.save()
                    data = { 'range_id' : beat.beat }
                    return Response(data,status=status.HTTP_200_OK)
                except Range.DoesNotExist:
                    error = {'error':'Invlid Range ID'}
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
            except Division.DoesNotExist :
                error = {'error':'Invalid Division ID'}
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
        except gisArea.DoesNotExist :
            error = {'error':'Invalid gisArea Id'}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    # Modify a Beat
    def patch(self,request):        
        beat_data =request.body
        beat_data = json.loads(beat_data)
        area_id = int(beat_data['gisArea'])
        range_id = int(beat_data['ranges'])
        beat_id  = int(beat_data['id'])
        division_id = int(beat_data['division'])
        try:
            beat = Beat.objects.get(beat=beat_id)
            try:
                ranges = Range.objects.get(ranges=range_id)
                try:
                    division = Division.objects.get(division=division_id)
                    try:
                        gisarea = gisArea.objects.get(gisarea=area_id)
                        updateparameters = {}
                        updateparameters['state'] = beat_data['state']
                        updateparameters['district'] = beat_data['district']
                        updateparameters['beat_name'] = beat_data['beat_name']
                        updateparameters['ranges'] = ranges
                        updateparameters['division'] = division
                        updateparameters['gisArea'] = gisarea
                        Beat.objects.filter(beat=beat_id).update(**updateparameters)
                        data = { 'beat_updated' : beat_id }
                        return Response(data,status=status.HTTP_200_OK)
                    except gisArea.DoesNotExist :
                        error = {'error':'Invalid gisArea Id'}
                        return Response(error,status=status.HTTP_400_BAD_REQUEST)
                except Division.DoesNotExist:
                    error = {'error':'Invalid Division Id'}
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
            except Range.DoesNotExist :
                error = {'error':'Invalid '}
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
        except Beat.DoesNotExist : 
            error = {'error':'Invalid Beat ID'}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BeatAPI,self).dispatch(*args, **kwargs)