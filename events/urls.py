from django.urls import path

from events import views

urlpatterns = [
    path('new_event/', views.new_event, name='new_event'),
    # path('my_meetings/', views.my_meetings, name='my_meetings'),
    path('events_list/', views.events_list, name='event_list'),
    # path('edit/<int:id>', views.meeting_edit, name='meeting_edit'),
    # path('delete/<int:id>', views.meeting_delete, name='meeting_list'),
]