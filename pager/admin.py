from django.contrib import admin

# Register your models here.

from .models import Device
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('nick', 'capcode')

admin.site.register(Device, DeviceAdmin)
