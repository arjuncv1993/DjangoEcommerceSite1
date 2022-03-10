from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userdetails(models.Model):
    username = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    Address_line1 = models.CharField(max_length=50, default='NULL')
    Address_line2 = models.CharField(max_length=50, default='NULL')
    City = models.CharField(max_length=50, default='NULL')
    State = models.CharField(max_length=50, default='NULL')
    Phone_no = models.TextField(max_length=10, default='NULL')
    Pincode = models.IntegerField()
    landmark = models.CharField(max_length=100, default='NULL')
    