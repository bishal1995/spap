from django.conf.urls import url
import views

urlpatterns = [

	# All order details	
    url(r'^dvision/$', views.PlantaeAPI.as_view() ),
]

