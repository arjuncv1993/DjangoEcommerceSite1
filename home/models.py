from django.db import models
from django.contrib.auth.models import User
from account.models import userdetails

# Create your models here.

class itemlist(models.Model):
    Item_No = models.IntegerField()
    Item_Name = models.CharField(max_length=50)
    Brand = models.CharField(max_length=25)
    Category = models.CharField(max_length=40)
    Sub_Category = models.CharField(max_length=50)
    Price = models.FloatField()
    Features = models.TextField(max_length=200)
    
    def __str__(self):
        return self.Item_Name


class cartitems(models.Model):
    username = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    Qty = models.IntegerField()
    Product_id = models.IntegerField()

