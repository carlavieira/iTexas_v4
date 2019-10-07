from django.contrib import admin
from .models import OfficeHour


# Register your models here.

class OfficeHoursAdmin(admin.ModelAdmin):
    list_display = ('member', 'date', 'checkin_time', 'checkout_time', 'duration')
    search_fields = ['member']


admin.site.register(OfficeHour, OfficeHoursAdmin)
