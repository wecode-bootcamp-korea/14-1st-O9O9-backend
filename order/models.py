from django.db import models

class OrderItem(models.Model):
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    order_item_quantity = models.IntegerField()
    order_item_price = models.CharField(max_length=80)
    order_shipment = models.CharField(max_length=100)


    class Meta:
        db_table = 'orderitems'

class Order(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    order_status = models.CharField(max_length=100)

    class Meta:
        db_table = 'orders'
