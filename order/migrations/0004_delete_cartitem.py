# Generated by Django 3.1.2 on 2020-11-24 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20201123_1156'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
