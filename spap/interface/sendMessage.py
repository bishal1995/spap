import requests
from django.conf import settings

def sendMessage(message,mobiles):
	if len(mobiles) > 0 and message:
		data = dict()
		proxies = {'http': "http://172.16.30.20:8080"}
		data['key'] = settings.SMS_KEY
		data['type'] = "text"
		data['senderid'] = settings.SMS_SENDER
		data['msg'] = message
		mobiles = ','.join(list(map(str, mobiles)))
		data['contacts'] = mobiles
		r = requests.get(settings.SMS_URL, params=data,proxies=proxies)
		return r
