from django.contrib import admin


# Register your models here.

class OfficeHoursAdmin(admin.ModelAdmin):
    fields = ('member', 'date', 'checkout_time', 'checkout_time')

