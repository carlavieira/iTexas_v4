from django.conf.urls import url
from django.urls import path

from office_hours import views

urlpatterns = [
    path('', views.check, name='check'),
    path('checkin/', views.checkin, name='checkin'),
    path('history/', views.history, name='office_hours_history'),

]
