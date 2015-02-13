from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	daily_kWh_target = models.DecimalField(max_digits=8, decimal_places=3, default=0)
	daily_cost_target = models.DecimalField(max_digits=8, decimal_places=3, default=0)
	hourly_kWh_max = models.DecimalField(max_digits=8, decimal_places=3, default=0)

	

def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)


import datetime
import hmac
import time
import uuid
from django.conf import settings
from django.db import models
try:
    from hashlib import sha1
except ImportError:
    import sha
    sha1 = sha.sha

class ApiKey(models.Model):
    user = models.OneToOneField(User, related_name='api_key')
    key = models.CharField(max_length=256, blank=True, default='')
    created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
    	return u"%s for %s" % (self.key, self.user)

    def save(self, *args, **kwargs):
    	if not self.key:
    		self.key = self.generate_key()

    	return super(ApiKey, self).save(*args, **kwargs)

    def generate_key(self):
    	# Get a random UUID.
    	new_uuid = uuid.uuid4()
    	# Hmac that beast.
    	return hmac.new(str(new_uuid), digestmod=sha1).hexdigest()


def create_api_key(sender, **kwargs):
	"""
	A signal for hooking up automatic ``ApiKey`` creation.
	"""
	if kwargs.get('created') is True:
		ApiKey.objects.create(user=kwargs.get('instance'))

models.signals.post_save.connect(create_api_key, sender=User)