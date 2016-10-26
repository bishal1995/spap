from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^$',UserFormView.as_view(),name="login"),
    url(r'^logOut$',LogOut.as_view(),name="logOut"),
    url(r'^dashboard/$',DashboardView.as_view(),name="dashboard"),
    url(r'^dashboard/usersactivity/(?P<activity>[\w-]+)/$',UserActivity.as_view(),name="useractivity"),
    url(r'^dashboard/species/(?P<bodytype>[\w-]+)/(?P<bodyId>[\d-]+)/$',SpeciesInfo.as_view(),name="species"),
    url(r'^dashboard/downloadCsvFile$',DownloadCsvFile.as_view(),name="downloadCsvFile"),
    url(r'^dashboard/sendnotification$',SendNotification.as_view(),name="sendNotification"),
    url(r'^dashboard/forest/beat/(?P<beatId>[\d-]+)/(?P<plantType>[\w-]+)/$',BeatInfo.as_view(),name="beatInfo"),
    url(r'^dashboard/forest/range/(?P<rangeId>[\d-]+)/(?P<plantType>[\w-]+)/$',RangeInfo.as_view(),name="rangeInfo"),
    url(r'^dashboard/forest/division/(?P<divisionId>[\d-]+)/(?P<plantType>[\w-]+)/$',DivisionInfo.as_view(),name="divisionInfo"),
]