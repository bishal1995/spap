from django.conf.urls import url
import views

urlpatterns = [

	# All order details	
    url(r'^plantaereg/$', views.RegPlantaeAPI.as_view() ),

]

