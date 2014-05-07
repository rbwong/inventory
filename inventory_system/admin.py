from django.contrib import admin
from inventory_system.models import Item, Customer, Supplier, ItemSupplied, PurchaseOrder, SalesInvoice

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'name', 'quantity', 'reorder_point', 'unit_price')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact', 'email')


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


class ItemSuppliedAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'item_name', 'date_created')

    def supplier_name(self, instance):
        return instance.supplier.name

    def item_name(self, instance):
        return instance.item.name


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('no', 'supplier_name', 'item_name', 'quantity', 'date_created')

    def supplier_name(self, instance):
        return instance.supplier.name

    def item_name(self, instance):
        return instance.item.name


class SalesInvoiceAdmin(admin.ModelAdmin):
    list_display = ('no', 'customer_name', 'item_name', 'quantity', 'date_created')

    def customer_name(self, instance):
        return instance.customer.name

    def item_name(self, instance):
        return instance.item.name

admin.site.register(Item, ItemAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(ItemSupplied, ItemSuppliedAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(SalesInvoice, SalesInvoiceAdmin)