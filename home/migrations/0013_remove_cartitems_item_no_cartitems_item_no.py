# Generated by Django 4.0 on 2022-03-06 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_cartitems_item_no_cartitems_item_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='Item_No',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='Item_No',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.itemlist'),
        ),
    ]
