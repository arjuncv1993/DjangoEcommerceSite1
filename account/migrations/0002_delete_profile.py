# Generated by Django 4.0 on 2022-02-28 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profile',
        ),
    ]