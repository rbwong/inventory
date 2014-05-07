from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
#from bulletin.views import BoardListView, BoardDetailView, ThreadDetailView, BoardCreateView, ThreadCreateView, UserProfileDetailView
from inventory_system import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.hello_world),
)
