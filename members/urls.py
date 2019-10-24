from django.conf.urls import url
from members import views
from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('', views.member_list, name='member_list'),
    path('view/<int:podio_code>', views.member_view, name='member_view'),
    path('edit/<int:podio_code>', views.member_update, name='member_edit'),
    path('delete/<int:podio_code>', views.member_delete, name='member_delete'),
    path('report/<int:podio_code>', views.member_report, name='member_report'),
    url(r'^reset-password/$', PasswordResetView.as_view(template_name='registration/password_reset_form.html')
        , name='reset_password'),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html')
        , name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html')
        , name='password_reset_confirm'),

    url(r'^reset-password/complete/$',
        PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
>>>>>>> 5f38753ddbd79dee10a902b9da9c15cca8ca0a8e
]
