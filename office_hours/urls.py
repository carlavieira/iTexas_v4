from django.conf.urls import url
from django.urls import path

from office_hours import views

urlpatterns = [
    path('', views.check, name='check'),
    path('checkin/', views.checkin, name='checkin'),
    path('checkout/', views.checkout, name='checkout'),
    path('myhistory/', views.myhistory, name='office_hours_history'),
    path('officehour_list/', views.officehour_list, name='officehour_list'),
    path('edit/<int:id>', views.officehour_update, name='officehour_edit'),
    path('delete/<int:id>', views.officehour_delete, name='officehour_delete'),

]
