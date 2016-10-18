from django.contrib import admin
from django.contrib.auth.models import User
from .models import LastActivity,DivisionOfficer,RangeOfficer,BeatOfficer
# Register your models here.
#admin.site.register(User)
admin.site.register(LastActivity)
admin.site.register(DivisionOfficer)
admin.site.register(RangeOfficer)
admin.site.register(BeatOfficer)