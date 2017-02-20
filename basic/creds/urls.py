from django.conf.urls import url, include
from django.contrib import admin

import creds.views as views 

urlpatterns = [

    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),

    url(r'^profile/', views.profile, name='profile'),
    url(r'^password-change/', views.password_change, name='password_change'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signup-confirm/(?P<uid>[0-9A-Za-z_\-]+)-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.signup_confirm, name='signup_confirm'),

    url(r'^success/', views.success, name='success'),
    url(r'^email-change/', views.email_change, name='email_change'),

    url(r'^password-reset-request/', views.password_reset_request,name='password_reset_request'),
    url(r'^password-reset/(?P<uid>[0-9A-Za-z_\-]+)-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.password_reset, name='password_reset'),
]
