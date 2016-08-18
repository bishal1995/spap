from django.conf.urls import url
from . import views

urlpatterns = [

	# All order details	
    url(r'^info/$', views.OfficerInfo.as_view() ),
]
