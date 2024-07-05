from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Supplier(models.Model): 
    name =models.CharField(max_length=50)
    contact_info= models.TextField(blank=True)

    def __str__(self):
       return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    order_number = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField()
    delivery_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100)
    items = models.ManyToManyField(InventoryItem, through='PurchaseOrderItem')

    def __str__(self):
        return self.order_number
 
class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)   

