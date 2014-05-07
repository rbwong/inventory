from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from inventory_system.views import *
from inventory_system import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.hello_world),
    url(r'^new_purchase_order/$', login_required(NewPurchaseOrderView.as_view())),
    url(r'^new_sales_invoice/$', login_required(NewSalesInvoiceView.as_view())),
    url(r'^purchase_order/$', login_required(PurchaseOrderListView.as_view())),
    url(r'^sales_invoice/$', login_required(SalesInvoiceListView.as_view())),
    url(r'^create_purchase_order$', views.hello_world),
)
