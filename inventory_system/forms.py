from django import forms
from django.contrib.auth.models import User
from inventory_system.models import Item, Customer, Supplier, ItemSupplied, PurchaseOrder, SalesInvoice
from django.utils import timezone

class PurchaseOrderForm(forms.ModelForm):
    no = forms.CharField(required=True)
    item_supplied = forms.ModelChoiceField(ItemSupplied.objects.all())
    quantity = forms.CharField(required=True)

    class Meta:
        model = PurchaseOrder
        fields = ('no', 'quantity')
'''
class ThreadCreationForm(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Thread
        fields = ('name',)

class PostCreationForm(forms.ModelForm):
    name = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('name', 'message')'''