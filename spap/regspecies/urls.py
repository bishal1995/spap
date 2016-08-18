from django.conf.urls import url
from . import views

urlpatterns = [

	# All order details	
    url(r'^plantaereg/$', views.RegPlantaeAPI.as_view() ),

]

