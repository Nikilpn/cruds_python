from django.db import models

# Create your models here.
class Employeedb(models.Model):
    NAME=models.CharField(max_length=100,null=True,blank=True)
    AGE=models.IntegerField(null=True,blank=True)
    MOBILE=models.IntegerField(null=True,blank=True)
    EMAILID=models.EmailField(max_length=100,null=True,blank=True)
    DEPARTMENT=models.CharField(max_length=100,null=True,blank=True)