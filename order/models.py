from django.db import models

class OrderItem(models.Model):
    product  = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    order    = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'orderitems'

class Order(models.Model):
    user         = models.ForeignKey('user.User', on_delete=models.CASCADE)
    order_number = models.CharField(max_length=100, null=True)
    order_date   = models.DateTimeField(auto_now_add=True)
    name         = models.CharField(max_length=100)
    address      = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    description  = models.CharField(max_length=100)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'orderstatuses'

class Shipment(models.Model):
    company_name    = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=100)

    class Meta:
        db_table = 'shipments'