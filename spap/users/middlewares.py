from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from users.models import LastActivity

# Update last activity for API calls via APP
class UpdateLastActivityMiddleWare(object):
	def process_request(self,request):
		if 'HTTP_AUTHORIZATION' in request.META:
			AuthToken = request.META['HTTP_AUTHORIZATION']
			AuthToken = AuthToken.replace('Token ','')
			user = Token.objects.get(key=AuthToken).user
			try:
				appuser = LastActivity.objects.get(user=user)
				lastactivity = LastActivity.objects.get(user=user)
				lastactivity.save()
				
			except LastActivity.DoesNotExist :
				LastActivity(
					user = user
				).save()
		else:
			pass