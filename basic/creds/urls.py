from django.conf.urls import url, include
from django.contrib import admin

import creds.views as views 

urlpatterns = [

    url(r'^login', views.login, name='login'),
    url(r'^logged_in', views.logged_in, name='logged_in'),
    url(r'^signup', views.signup, name='signup')

]
