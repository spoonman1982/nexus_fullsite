from django.contrib import admin
from userprofile.models import UserProfile, ApiKey
from readings.models import Device, CurrentReading, HourlyReading, DailyReading, MonthlyReading
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


class UserProfileAdmin(admin.ModelAdmin):
	pass
admin.site.register(UserProfile, UserProfileAdmin)


class ApiKeyAdmin(admin.ModelAdmin):
	pass
admin.site.register(ApiKey, ApiKeyAdmin)


class DeviceAdmin(admin.ModelAdmin):
	pass
admin.site.register(Device, DeviceAdmin)


class CurrentReadingAdmin(admin.ModelAdmin):
	pass
admin.site.register(CurrentReading, CurrentReadingAdmin)


class HourlyReadingAdmin(admin.ModelAdmin):
	pass
admin.site.register(HourlyReading, HourlyReadingAdmin)


class DailyReadingAdmin(admin.ModelAdmin):
	pass
admin.site.register(DailyReading, DailyReadingAdmin)


class MonthlyReadingAdmin(admin.ModelAdmin):
	pass
admin.site.register(MonthlyReading, MonthlyReadingAdmin)