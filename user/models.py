from django.db import models

class User(models.Model):
    username_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()

    class Meta:
        db_table = 'users'

