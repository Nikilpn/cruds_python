from django.db import models

# Create your models here.
class EmployeeDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Age=models.IntegerField(null=True,blank=True)
    Place=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.Name