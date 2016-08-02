from django.conf.urls import url
import views

urlpatterns = [

	# All order details	
    url(r'^plantaeImg/$', views.ImageUploadAPI.as_view() ),

]

