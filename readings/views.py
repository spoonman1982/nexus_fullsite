import json
from json import dumps, loads, JSONEncoder
from datetime import datetime, date, time, timedelta
from django.db.models.query import QuerySet
from django.core.serializers import serialize
from django.http import HttpResponse
from readings.models import HourlyReading, DailyReading, MonthlyReading, Device
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from userprofile.models import UserProfile, ApiKey
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


def hourly_readings_view(request):

	if request.user.id:
		current_device = Device.objects.get(user = request.user.id)
		hourly_reading_list = HourlyReading.objects.filter(device=current_device)
		return render_to_response("readings/hourly_readings.html", {
	        'hourly_reading_list':hourly_reading_list
	    },context_instance=RequestContext(request))
	else:
		return render_to_response('readings/hourly_readings.html', {})

def weekly_readings_view(request):
	return render_to_response('readings/weekly_readings.html', {})

def monthly_readings_view(request):
	return render_to_response('readings/monthly_readings.html', {})



def hourly_readings_list(request):
	if request.method == 'POST':
		response_data={}
		readings = HourlyReading.objects.filter(device = find_device(request.body), time__range=("2014-10-28T00:00:00", "2014-10-28T12:00:00"))
		response_data['objects'] = readings
		return HttpResponse(json.dumps(readings, cls=DjangoJSONEncoder), content_type="application/json")

def weekly_readings_list(request):
	readings = DailyReading.objects.filter(time__range=("2014-10-05T00:00:00", "2014-10-11T00:00:00")) #device = find_device(request.body),
	response_data={}
	response_data['objects'] = readings
	return HttpResponse(json.dumps(readings, cls=DjangoJSONEncoder), content_type="application/json")

def monthly_readings_list(request):
	readings = DailyReading.objects.filter(time__range=("2014-10-01T00:00:00", "2014-10-31T00:00:00")) #device = find_device(request.body),
	response_data={}
	response_data['objects'] = readings
	return HttpResponse(json.dumps(readings, cls=DjangoJSONEncoder), content_type="application/json")

def yearly_readings_list(request):
	return HttpResponse("OK")


def find_device(data):
	"""
	Finds the device to retrieve the readings from depending on the
	user api_key sent via request
	"""
	api_key = simplejson.loads(data)["api_key"]
	current_user = User.objects.filter(api_key__key = api_key)[0]
	return current_user.device





