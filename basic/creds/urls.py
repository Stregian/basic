from django.conf.urls import url, include
from django.contrib import admin

import creds.views as views 

urlpatterns = [

    url(r'^login', views.login, name='login'),
    url(r'^logged_in', views.logged_in, name='logged_in'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^password_change', views.password_change, name='password_change'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^password_reset_start', views.password_reset_start,name='password_reset_start')
]
