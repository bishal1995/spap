import csv
from django.utils import timezone
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
#imports from apps
from .forms import UserForm
from .sendMessage import sendMessage
from departments.models import Beat,Range,Division
from regspecies.models import RegPlantae
from resourcebank.models import SeedDeposit
from users.models import LastActivity

class UserFormView(View):
	form_class= UserForm
	template_name = "login.html"

	def get(self,request):
		if request.user.is_authenticated:
			return redirect("interface:dashboard")
		else:	
			form = self.form_class(None)
			context = {
				'form': form,
				'auth_failed': False,
			}
			return render(request,self.template_name,context)
	def post(self,request):
		username = request.POST.get('username')
		password = request.POST.get('password')	
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("interface:dashboard")
		form = self.form_class(request.POST or None)
		context = {
			'form': form,
			'auth_failed': True,
		}				 
		return render(request,self.template_name,context)
		

class DashboardView(View):
	template_name = "dashboard.html"
	def get(self,request):
		if request.user.is_authenticated:
			total_active_users = LastActivity.objects.filter(last_activity__gte=timezone.now()-timezone.timedelta(hours=5)).count()
			total_inactive_users = LastActivity.objects.filter(last_activity__lte=timezone.now()-timezone.timedelta(hours=5)).count()
			context = {
				"total_active_users": total_active_users,
				"total_inactive_users" : total_inactive_users,
			}
			return render(request,self.template_name,context)
		else:
			return redirect("interface:login")	
class UserActivity(View):
	template_name = "userActivity.html"
	def get(self,request,activity="active"):
		if activity=="active":
			active_users = LastActivity.objects.filter(last_activity__gte=timezone.now()-timezone.timedelta(hours=5))
			paginator = Paginator(active_users, 1) 
			page = request.GET.get('page')
			try:
				object_list = paginator.page(page)
			except PageNotAnInteger:
				object_list = paginator.page(1)
			except EmptyPage:
				object_list = paginator.page(paginator.num_pages)
			context = {
				"object_list": object_list,
				"table_heading": "Active Users",
				"inactive":False,
			}
		else:
			inactive_users = LastActivity.objects.filter(last_activity__lte=timezone.now()-timezone.timedelta(hours=5))
			paginator = Paginator(inactive_users, 1) 
			page = request.GET.get('page')
			try:
				object_list = paginator.page(page)
			except PageNotAnInteger:
				object_list = paginator.page(1)
			except EmptyPage:
				object_list = paginator.page(paginator.num_pages)
			context = {
				"object_list": object_list,
				"table_heading": "Inactive Users",
				"inactive": True,
			}	
		return render(request,self.template_name,context)

class SpeciesInfo(ListView):
	template_name = "species.html"
	model = SeedDeposit
	context_object_name = "object_list"
	paginate_by = 1
	def get_queryset(self):
		if self.kwargs['bodytype']=="range":
			body_id = int(self.kwargs['bodyId'])
			if body_id=="":
				body_id = 1
			queryset = SeedDeposit.objects.filter(body_type="RN",body_id=body_id)
		elif self.kwargs['bodytype']=="division":
			body_id = self.kwargs['bodyId']
			if body_id=="":
				body_id = 1
			queryset = SeedDeposit.objects.filter(body_type="DI",body_id=body_id)
		else:
			body_id = self.kwargs['bodyId']
			if body_id=="":
				body_id = 1	
			queryset = SeedDeposit.objects.filter(body_type="BT",body_id=body_id)
		return queryset
	def get_context_data(self,**kwargs):
		context = super(SpeciesInfo, self).get_context_data(**kwargs)
		body_type = self.kwargs['bodytype']
		if body_type == "beat":	
			idList = Beat.objects.all()
		elif body_type == "range":
			idList = Range.objects.all()
		else:
			idList = Division.objects.all()		
		context.update({
			'idList':idList,
			'queryset' : self.queryset,
			'department' : 'Beat Id'
			})
		#print beatIdList
		return context	

class BeatInfo(ListView):
	template_name = "registeredPlants.html"
	model = RegPlantae
	context_object_name = "object_list"
	paginate_by = 2
	queryset = {}
	def get_queryset(self):
		plantType = self.kwargs['plantType']
		beatId = self.kwargs['beatId']
		if beatId=="":
			beatId = 1
		if plantType =="":
			plantType = "SB"
		self.queryset = RegPlantae.objects.filter(beat_id=beatId,ptype=plantType)			
		return self.queryset
	
	def get_context_data(self,**kwargs):
		context = super(BeatInfo, self).get_context_data(**kwargs)
		beatIdList = Beat.objects.all()
		context.update({
			'idList': beatIdList,
			'queryset' : self.queryset,
			'department' : 'Beat Id'
			})
		#print beatIdList
		return context

class RangeInfo(ListView):
	template_name = "registeredPlants.html"
	model = RegPlantae
	context_object_name = "object_list"
	paginate_by = 2
	queryset = {}
	def get_queryset(self):
		plantType = self.kwargs['plantType']
		rangeId = self.kwargs['rangeId']
		if rangeId=="":
			rangeId = 1
		if plantType =="":
			plantType = "SB"
		beatIds = Beat.objects.filter(ranges_id=rangeId)
		self.queryset = RegPlantae.objects.filter(beat__in=beatIds)
		return self.queryset
	
	def get_context_data(self,**kwargs):
		context = super(RangeInfo, self).get_context_data(**kwargs)
		rangeIdList = Range.objects.all()
		context.update({
			'idList': rangeIdList,
			'queryset' : self.queryset,
			'department' : 'Range Id'
			})
		return context


class DivisionInfo(ListView):
	template_name = "registeredPlants.html"
	model = RegPlantae
	context_object_name = "object_list"
	paginate_by = 2
	queryset = {}
	def get_queryset(self):
		plantType = self.kwargs['plantType']
		divisionId = self.kwargs['divisionId']
		if divisionId=="":
			divisionId = 1
		if plantType =="":
			plantType = "SB"
		beatIds = Beat.objects.filter(division_id=divisionId)
		self.queryset = RegPlantae.objects.filter(beat__in=beatIds)
		return self.queryset
	
	def get_context_data(self,**kwargs):
		context = super(DivisionInfo, self).get_context_data(**kwargs)
		divisionIdList = Division.objects.all()
		context.update({
			'idList': divisionIdList,
			'queryset' : self.queryset,
			'department' : 'Division Id'
			})
		return context

class DownloadCsvFile(View):	
	def get(self,request):
		response = HttpResponse (content_type='text/csv')
		writer = csv.writer(response)
		writer.writerows(SeedDeposit.objects.values_list('state','account','body_id','balance','last_updated_date'))
		return response

class SendNotification(View):
	def get(self,request):
		#sendMessage("hello","9085958622")
		return redirect("interface:dashboard")

class LogOut(View):
	def get(self,request):
		logout(request)
		return redirect("interface:login")		

class DetailInfoPlants(View):
	template_name = "detailViewOfPlant.html"
	context_object_name = "object_list"
	def get(self,request,plantId=1):
		obj = RegPlantae.objects.get(regplantae=plantId)
		context = {
			'obj': obj
		}
		return render(request,self.template_name,context)