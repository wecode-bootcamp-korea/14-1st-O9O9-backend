from django.db import models

class Product(models.Model):
    maincategory       = models.ForeignKey('MainCategory', on_delete=models.CASCADE, null=True)
    subcategory        = models.ForeignKey('SubCategory', on_delete=models.CASCADE, null=True)
    subsubcategory     = models.ForeignKey('SubSubCategory', on_delete=models.CASCADE, null=True)
    name               = models.CharField(max_length=100)
    brand              = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True)
    price              = models.CharField(max_length=80, null=True)
    more_information   = models.TextField()
    seller_information = models.TextField()
    exchange           = models.TextField()
    thumbnail_image    = models.URLField(max_length=500)
    detail_image       = models.URLField(max_length=500)
    essential          = models.BooleanField(null=True)
    optional           = models.BooleanField(null=True)
    productgroup       = models.ForeignKey('Productgroup', on_delete=models.CASCADE, null = True)

    class Meta:
        db_table = 'products'

class Brand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'brands'

class ProductGroup(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        db_table = 'productgroups'

class MainCategory(models.Model):
    name = models.CharField(max_length=80)

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

class WatchList(models.Model):
    user    = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'watchlists'