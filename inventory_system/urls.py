from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from inventory_system.views import NewPurchaseOrderView
from inventory_system import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.hello_world),
    url(r'^new_purchase_order/$', login_required(NewPurchaseOrderView.as_view())),
    url(r'^create_purchase_order$', views.hello_world),
)
