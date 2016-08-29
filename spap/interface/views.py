from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.list import ListView
from .forms import UserForm


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
		print request.user.last_login
		if request.user.is_authenticated:
			return render(request,self.template_name,{})
		else:
			return redirect("interface:login")	

class LogOut(View):
	def get(self,request):
		logout(request)
		return redirect("interface:login")		