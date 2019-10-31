from django.contrib import admin

# Register your models here.
from events.models import Event


class EventsAdmin(admin.ModelAdmin):
    list_display = ('type', 'leader', 'date', 'time')


admin.site.register(Event, EventsAdmin)