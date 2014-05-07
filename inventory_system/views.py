from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from inventory_system.models import Item, Customer, Supplier, ItemSupplied, PurchaseOrder, SalesInvoice
from inventory_system.forms import PurchaseOrderForm, SalesInvoiceForm
from django.db.models import F

class NewPurchaseOrderView(CreateView):
    template_name = 'inventory_system/new_purchase_order.html'
    form_class = PurchaseOrderForm
    success_url = '/'

    def get_form(self, form_class):
        form = super(NewPurchaseOrderView, self).get_form(form_class)
        if self.request.GET.get('item'):
            item = get_object_or_404(Item, item_code=self.request.GET.get('item'))
            item_supplied = ItemSupplied.objects.filter(item=item)
            form.fields['item_supplied'].queryset = item_supplied

        return form

    def form_valid(self, form):
        item_supplied = ItemSupplied.objects.get(id=form.data['item_supplied'])
        form.instance.item = item_supplied.item
        form.instance.supplier = item_supplied.supplier

        item_supplied.item.quantity += form.instance.quantity
        item_supplied.item.save()
        return super(NewPurchaseOrderView, self).form_valid(form)

class NewSalesInvoiceView(CreateView):
    template_name = 'inventory_system/new_sales_invoice.html'
    form_class = SalesInvoiceForm
    success_url = '/'

    def get_form(self, form_class):
        form = super(NewSalesInvoiceView, self).get_form(form_class)
        if self.request.GET.get('item'):
            item = get_object_or_404(Item, item_code=self.request.GET.get('item'))
            form.fields['item'].initial = item

        return form

    def form_valid(self, form):
        form.instance.item.quantity -= form.instance.quantity
        form.instance.item.save()
        return super(NewSalesInvoiceView, self).form_valid(form)


class PurchaseOrderListView(ListView):
    
    queryset = PurchaseOrder.objects.order_by('-date_created')
    template_name = 'inventory_system/purchase_order_list.html'

    def get_context_data(self, **kwargs):
        context = super(PurchaseOrderListView, self).get_context_data(**kwargs)
        return context


class SalesInvoiceListView(ListView):
    
    queryset = SalesInvoice.objects.order_by('-date_created')
    template_name = 'inventory_system/sales_invoice_list.html'

    def get_context_data(self, **kwargs):
        context = super(SalesInvoiceListView, self).get_context_data(**kwargs)
        return context


class ReorderListView(ListView):
    
    queryset = Item.objects.filter(quantity__lte=F('reorder_point')).order_by('-date_created')
    template_name = 'inventory_system/reorder_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReorderListView, self).get_context_data(**kwargs)
        return context


class ItemListView(ListView):
    
    queryset = Item.objects.all().order_by('-date_created')
    template_name = 'inventory_system/item_list.html'

    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        return context


class ItemDetailView(DetailView):
    template_name = 'inventory_system/item.html'

    def get_object(self):
        return get_object_or_404(Item, item_code=self.args[0])

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['sales_invoice_list'] = SalesInvoice.objects.filter(item=self.object).order_by('-date_created')
        context['item_supplied'] = ItemSupplied.objects.filter(item=self.object).order_by('-date_created')
        context['purchase_order_list'] = PurchaseOrder.objects.filter(item=self.object).order_by('-date_created')
        return context