# Generated by Django 3.1.2 on 2020-11-24 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_checkid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CheckId',
        ),
    ]