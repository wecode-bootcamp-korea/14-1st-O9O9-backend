from django.db import models

class Product(models.Model):
    name               = models.CharField(max_length=100)
    brand              = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True)
    price              = models.CharField(max_length=80, null=True)
    more_information   = models.TextField(null=True)
    seller_information = models.TextField(null=True)
    exchange           = models.TextField(null=True)
    thumbnail_image    = models.URLField(max_length=500,null=True)
    detail_image       = models.URLField(max_length=500,null=True)
    essential          = models.BooleanField(null=True)
    optional           = models.BooleanField(null=True)
    productgroup       = models.ForeignKey('Productgroup', on_delete=models.CASCADE, null = True)  
    maincategory       = models.ForeignKey('MainCategory', on_delete=models.CASCADE, null=True)
    subcategory        = models.ForeignKey('SubCategory', on_delete=models.CASCADE, null=True)
    subsubcategory     = models.ForeignKey('SubSubCategory', on_delete=models.CASCADE, null=True)
    buy_count          = models.ManyToManyField('user.User', related_name='buy_product', null=True)
    watchlist          = models.ManyToManyField('user.User', related_name='watch_product', null=True)

    class Meta:
        db_table = 'products'

class Brand(models.Model):
    name = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = 'brands'

class ProductGroup(models.Model):
    name = models.CharField(max_length=80,null=True)

    class Meta:
        db_table = 'productgroups'

class MainCategory(models.Model):
    name = models.CharField(max_length=80,null=True)

    class Meta:
        db_table = 'maincategories'

class SubCategory(models.Model):
    name = models.CharField(max_length=80,null=True)

    class Meta:
        db_table = 'subcategories'

class SubSubCategory(models.Model):
    name = models.CharField(max_length=80,null=True)

    class Meta:
        db_table = 'subsubcategories'
