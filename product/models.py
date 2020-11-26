from django.db import models

class Product(models.Model):
    name               = models.CharField(max_length=100)
    brand              = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True)
    price              = models.CharField(max_length=80, null=True)
    more_information   = models.ForeignKey('MoreInformation', on_delete=models.CASCADE, null=True)
    seller_information = models.ForeignKey('SellerInformation', on_delete=models.CASCADE, null=True)
    exchange           = models.ForeignKey('Exchange', on_delete=models.CASCADE, null=True)
    thumbnail_image    = models.URLField(max_length=500)
    detail_image       = models.URLField(max_length=500)
    essential          = models.BooleanField()
    optional           = models.BooleanField()
    productgroup       = models.ForeignKey('ProductGroup', on_delete=models.CASCADE, null=True)
    maincategory       = models.ForeignKey('MainCategory', on_delete=models.CASCADE, null=True)
    subcategory        = models.ForeignKey('SubCategory', on_delete=models.CASCADE, null=True)
    subsubcategory     = models.ForeignKey('SubSubCategory', on_delete=models.CASCADE, null=True)
    buy_count          = models.IntegerField()
    watchlist          = models.ManyToManyField('user.User', related_name='watch_product', through='BuyCount')

    class Meta:
        db_table = 'products'

class Brand(models.Model):
    name = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = 'brands'

class ProductGroup(models.Model):
    name = models.CharField(max_length=80, null=True)

    class Meta:
        db_table = 'productgroups'

class MainCategory(models.Model):
    name = models.CharField(max_length=80,null=True)

    class Meta:
        db_table = 'maincategories'

class SubCategory(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        db_table = 'subcategories'

class SubSubCategory(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        db_table = 'subsubcategories'

class MoreInformation(models.Model):
    tax_status              = models.CharField(max_length=100)
    receipt                 = models.CharField(max_length=100)
    business_classification = models.CharField(max_length=100)
    producer_importer       = models.CharField(max_length=100)
    origin                  = models.CharField(max_length=100)
    manufacturing_date      = models.CharField(max_length=100)
    shelf_life              = models.CharField(max_length=100)
    storage_method          = models.CharField(max_length=100)
    delivery_period         = models.CharField(max_length=100)

class SellerInformation(models.Model):
    representative  = models.CharField(max_length=100)
    business_number = models.CharField(max_length=100)
    phone_number    = models.CharField(max_length=100)
    email           = models.CharField(max_length=100)

class Exchange(models.Model):
    return_shipping_fee = models.CharField(max_length=100)
    where_to_send       = models.CharField(max_length=100)
    detail_information  = models.CharField(max_length=2000)

class WatchList(models.Model):
    user    = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
