from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from inventory_system.views import *
from inventory_system import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', login_required(ItemListView.as_view())),
    url(r'^customers$', login_required(CustomerListView.as_view())),
    url(r'^suppliers$', login_required(SupplierListView.as_view())),
    url(r'^new_purchase_order/$', login_required(NewPurchaseOrderView.as_view())),
    url(r'^new_sales_invoice/$', login_required(NewSalesInvoiceView.as_view())),
    url(r'^purchase_order/$', login_required(PurchaseOrderListView.as_view())),
    url(r'^sales_invoice/$', login_required(SalesInvoiceListView.as_view())),
    url(r'^reorder_items/$', login_required(ReorderListView.as_view())),
    url(r'^item/([\w-]+)/$', login_required(ItemDetailView.as_view())),
    url(r'^customer/([\w-]+)/$', login_required(CustomerDetailView.as_view())),
    url(r'^supplier/([\w-]+)/$', login_required(SupplierDetailView.as_view())),
)
