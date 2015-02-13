import json
from json import dumps, loads, JSONEncoder
from datetime import datetime, date, time, timedelta
from django.db.models.query import QuerySet
from django.core.serializers import serialize
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from userprofile.models import UserProfile, ApiKey
from django.core.context_processors import csrf
from django.utils import simplejson


today = date.today()

now = datetime.now()

class DjangoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            # `default` must return a python serializable
            # structure, the easiest way is to load the JSON
            # string produced by `serialize` and return it
            return loads(serialize('json', obj))
        return JSONEncoder.default(self,obj)
        

def login(request):
	return render_to_response('login.html', {})


def auth_view(request):
	if request.method == 'POST':
		print "Works on this end"
		data = simplejson.loads(request.body)
		user = auth.authenticate(username=data['username'], password=data['password'])
		response_data={}
		print user.username
		if user is not None:
			response_data['api_key'] = user.api_key.key
			response_data['username'] = user.username
	return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")



def logged_in(request):
	return render_to_response('logged_in.html',
		{'full_name': request.user.username})

def invalid(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')