from django.conf.urls import patterns, include, url



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),

	#user interface
	url(r'^$', 'readings.views.hourly_readings_view',  name='home'),
	#url(r'^hourlyReadingsList/$', 'readings.views.hourly_readings_list', name="readings_list"),
	url(r'^hourlyreadingslist/$', 'readings.views.hourly_readings_list'),
	url(r'^weeklyreadingslist/$', 'readings.views.weekly_readings_list'),
	url(r'^monthlyreadingslist/$', 'readings.views.monthly_readings_list'),
	url(r'^yearlyreadingslist/$', 'readings.views.yearly_readings_list'),

	url(r'^accounts/login/$', 'nexus_fullsite.views.login'),
	url(r'^accounts/auth/$', 'nexus_fullsite.views.auth_view'),
	url(r'^accounts/logout/$', 'nexus_fullsite.views.logout'),
	url(r'^accounts/logged_in/$', 'nexus_fullsite.views.logged_in'),
	url(r'^accounts/invalid/$', 'nexus_fullsite.views.invalid'),


    # Examples:
    # url(r'^$', 'nexus_fullsite.views.home', name='home'), (device = request.user.device, time__lte = (now + timedelta(days=1)), time__gte = now)
    # url(r'^nexus_fullsite/', include('nexus_fullsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
