from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from inventory_system.models import Item, Customer, Supplier, ItemSupplied, PurchaseOrder, SalesInvoice
from inventory_system.forms import PurchaseOrderForm

@login_required
def hello_world(request):
    return HttpResponse("Hello, world.")


class NewPurchaseOrderView(CreateView):
    template_name = 'inventory_system/new_purchase_order.html'
    form_class = PurchaseOrderForm
    success_url = '/'

    def form_valid(self, form):
    	item_supplied = ItemSupplied.objects.get(id=form.data['item_supplied'])
        form.instance.item = item_supplied.item
        form.instance.supplier = item_supplied.supplier

        item_supplied.item.quantity += form.instance.quantity
        item_supplied.item.save()
        return super(NewPurchaseOrderView, self).form_valid(form)