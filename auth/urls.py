from django.conf.urls import patterns, include, url
from auth import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
)
