from django.conf.urls import url
from members import views

# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url('register/', views.register, name='register'),
    url('user_login/', views.user_login, name='user_login'),
    url('user_logout/', views.user_logout, name='user_logout'),
]