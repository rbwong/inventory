from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    item_code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    reorder_point = models.IntegerField()
    unit_price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class ItemSupplied(models.Model):
    supplier = models.ForeignKey(Supplier)
    item = models.ForeignKey(Item)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.supplier.name + ' - ' + self.item.name


class PurchaseOrder(models.Model):
    no = models.IntegerField(unique=True)
    supplier = models.ForeignKey(Supplier)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if self.pk is None:
            super(PurchaseOrder, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.supplier.name + ' - ' + self.item.name


class SalesInvoice(models.Model):
    no = models.IntegerField(unique=True)
    customer = models.ForeignKey(Customer)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if self.pk is None:
            super(SalesInvoice, self).save(*args, **kwargs)