from django.db import models
from django.contrib.auth.models import User



class Device(models.Model):
	user = models.OneToOneField(User, unique=True, primary_key=True, related_name="device")
	device_identifier = models.CharField(max_length= 16)

	class Meta():
		verbose_name = 'device'

	def __unicode__(self):
		return self.device_identifier


class CurrentReading(models.Model):
	device = models.ForeignKey(Device, related_name="current_readings")
	kWh = models.DecimalField(max_digits=6, decimal_places=4)
	cost  = models.DecimalField(max_digits=6, decimal_places=4)
	created_at= models.DateTimeField(auto_now_add=True)
	time = models.DateTimeField('time period')

	class Meta():
		verbose_name = 'current_reading'

	def __unicode__(self):
		return u"%s for %s" % (self.time.strftime('%Y-%m-%d %I:%M%p'), self.device)


class HourlyReading(models.Model):
	device = models.ForeignKey(Device, related_name="hourly_readings")
	kWh = models.DecimalField(max_digits=6, decimal_places=4)
	cost  = models.DecimalField(max_digits=6, decimal_places=4)
	created_at= models.DateTimeField(auto_now_add=True)
	time = models.DateTimeField('time period')
	#device_name = device_identifier

	class Meta():
		verbose_name = 'hourly_reading'

	def __unicode__(self):
		return u"%s for %s" % (self.time.strftime('%Y-%m-%d %I:%M%p'), self.device)


class DailyReading(models.Model):
	device = models.ForeignKey(Device, related_name="daily_readings")
	kWh = models.DecimalField(max_digits=6, decimal_places=4)
	cost  = models.DecimalField(max_digits=6, decimal_places=4)
	created_at= models.DateTimeField(auto_now_add=True)
	time = models.DateTimeField()

	class Meta():
		verbose_name = 'daily_reading'

	def __unicode__(self):
		return self.time.strftime('%Y-%m-%d')


class MonthlyReading(models.Model):
	device = models.ForeignKey(Device, related_name="monthly_readings")
	kWh = models.DecimalField(max_digits=6, decimal_places=4)
	cost  = models.DecimalField(max_digits=6, decimal_places=4)
	created_at= models.DateTimeField(auto_now_add=True)
	time = models.DateTimeField()

	class Meta():
		verbose_name = 'monthly_reading'

	def __unicode__(self):
		return self.time.strftime('%Y-%m-%d')
