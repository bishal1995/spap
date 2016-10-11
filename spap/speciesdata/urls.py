from django.conf.urls import url
from . import views

urlpatterns = [

	# All order details	
    url(r'^plantae/$', views.PlantaeAPI.as_view() ),
    url(r'^plantaelist/$', views.PlantaeListAPI.as_view() ),
]

