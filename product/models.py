from django.db import models

class Product(models.Model):
    name               = models.CharField(max_length=100)
    brand              = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True)
    more_information   = models.TextField()
    seller_information = models.TextField()
    exchange           = models.TextField()
    thumbnail_image    = models.URLField(max_length=500)
    detail_image       = models.URLField(max_length=500)
    essencial          = models.BooleanField()
    optional           = models.BooleanField()
    productgroup       = models.ForeignKey('Productgroup', on_delete=models.CASCADE)
    subsubcategy       = models.ForeignKey('SubSubCategory', on_delete=models.CASCADE)
    buy_count          = models.IntegerField()
    watch_count        = models.IntegerField()

    class Meta:
        db_table = 'products'

class Brand(models.Model):
    name = models.CharField(max_length=100)

class ProductGroup(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        db_table = 'productgroups'

class MainCategory(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        db_table = 'maincategories'

class SubCategory(models.Model):
    name            = models.CharField(max_length=80)
    maincategory    = models.ForeignKey('MainCategory', on_delete=models.CASCADE)

    class Meta:
        db_table = 'subcategories'

class SubSubCategory(models.Model):
    name           = models.CharField(max_length=80)
    subcategory    = models.ForeignKey('SubCategory', on_delete=models.CASCADE)

    class Meta:
        db_table = 'subsubcategories'

class WatchList(models.Model):
    user    = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'watchlists'

class PhotoReview(models.Model):
    user        = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product     = models.ForeignKey('Product', on_delete=models.CASCADE)
    image_url   = models.URLField(max_length=500)
    title       = models.CharField(max_length=200)
    content     = models.CharField(max_length=200)
    create_at   = models.DateTimeField(auto_now_add=True)
    view_count  = models.IntegerField()

    class Meta:
        db_table = 'photoreviews'

class Review(models.Model):
    user         = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product      = models.ForeignKey('Product', on_delete=models.CASCADE)
    satisfaction = models.CharField(max_length=2000)
    content      = models.CharField(max_length=50)
    create_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviews'

class Question(models.Model):
    user          = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product       = models.ForeignKey('Product', on_delete=models.CASCADE)
    title         = models.CharField(max_length=100)
    content       = models.CharField(max_length=100)
    question_type = models.CharField(max_length=2000)
    answer_status = models.CharField(max_length=2000)
    create_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'questions'