from django.conf.urls import url,include
from .views import UserFormView,DashboardView,LogOut,UserActivity,SpeciesInfo,DownloadCsvFile,SendNotification,RegisteredPlants

urlpatterns = [
    url(r'^$',UserFormView.as_view(),name="login"),
    url(r'^logOut$',LogOut.as_view(),name="logOut"),
    url(r'^dashboard/$',DashboardView.as_view(),name="dashboard"),
    url(r'^dashboard/usersactivity/(?P<activity>[\w-]+)/$',UserActivity.as_view(),name="useractivity"),
    url(r'^dashboard/species/(?P<bodytype>[\w-]+)/$',SpeciesInfo.as_view(),name="species"),
    url(r'^dashboard/downloadCsvFile$',DownloadCsvFile.as_view(),name="downloadCsvFile"),
    url(r'^dashboard/sendnotification$',SendNotification.as_view(),name="sendNotification"),
    url(r'^dashboard/registeredplants$',RegisteredPlants.as_view(),name="registeredPlants"),
]