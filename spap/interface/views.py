import csv
from django.utils import timezone
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.list import ListView
from .forms import UserForm
from users.models import LastActivity
from resourcebank.models import SeedDeposit
from .sendMessage import sendMessage

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
		#print self.kwargs['bodytype']
		if self.kwargs['bodytype']=="range":
			queryset = SeedDeposit.objects.filter(body_type="RN")
		elif self.kwargs['bodytype']=="division":
			queryset = SeedDeposit.objects.filter(body_type="DI")
		else:
			queryset = SeedDeposit.objects.filter(body_type="BT")		
		return queryset	

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