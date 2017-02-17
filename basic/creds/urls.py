from django.conf.urls import url, include
from django.contrib import admin

import creds.views as views 

urlpatterns = [

    url(r'^login/', views.login, name='login'),
    
    url(r'^logged-in', views.logged_in, name='logged_in'),
    

    url(r'^profile/', views.profile, name='profile'),
    url(r'^password-change/', views.password_change, name='password-change'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'success/', views.success, name='success'),

    url(r'^password-reset-request/', views.password_reset_request,name='password-reset-request'),
    url(r'^password-reset/(?P<uid>[0-9A-Za-z_\-]+)-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.password_reset, name='password_reset'),
]
