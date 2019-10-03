from django.conf.urls import url
from members import views
from django.urls import path

# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url('register/', views.register, name='register'),
    url('user_login/', views.user_login, name='user_login'),
    url('user_logout/', views.user_logout, name='user_logout'),
    path('', views.member_list, name='member_list'),
    path('view/<int:podio_code>', views.member_view, name='member_view'),
    path('edit/<int:podio_code>', views.member_update, name='member_edit'),
    path('delete/<int:podio_code>', views.member_delete, name='member_delete'),
]
