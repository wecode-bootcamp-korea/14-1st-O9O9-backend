from django.db import models

class PhotoReview(models.Model):
    user         = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product      = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    image_url    = models.URLField(max_length=500)
    title        = models.CharField(max_length=200)
    content      = models.CharField(max_length=200)
    created_at   = models.DateTimeField(auto_now_add=True)
    view_count   = models.IntegerField()

    class Meta:
        db_table = 'photoreviews'

class Review(models.Model):
    user          = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product       = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    satisfaction  = models.CharField(max_length=2000)
    content       = models.CharField(max_length=50)
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviews'

class Question(models.Model):
    user           = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product        = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    title          = models.CharField(max_length=100)
    content        = models.CharField(max_length=100)
    question_type  = models.CharField(max_length=2000)
    answer_status  = models.CharField(max_length=2000)
    created_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'questions'