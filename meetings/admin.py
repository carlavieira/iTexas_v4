from django.contrib import admin
from meetings.models import Meeting


# Register your models here.

class MeetingsAdmin(admin.ModelAdmin):
    list_display = ('type', 'leader', 'date', 'time')


admin.site.register(Meeting, MeetingsAdmin)
