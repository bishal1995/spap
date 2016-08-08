from django.conf.urls import url
import views

urlpatterns = [

	# All order details	
    url(r'^info/$', views.OfficerInfo.as_view() ),
]
