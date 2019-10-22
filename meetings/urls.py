from django.urls import path

from meetings import views

urlpatterns = [
    path('new_meeting/', views.new_meeting, name='new_meeting'),
    path('my_meetings/', views.my_meetings, name='my_meetings'),
    path('meetings_list/', views.meetings_list, name='meeting_list'),
    path('edit/<int:id>', views.meeting_edit, name='meeting_edit'),
    path('delete/<int:id>', views.meeting_delete, name='meeting_list'),
]
