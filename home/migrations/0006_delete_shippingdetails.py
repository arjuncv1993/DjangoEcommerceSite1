# Generated by Django 4.0 on 2022-03-06 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_shippingdetails_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='shippingdetails',
        ),
    ]
