from django.db import models

# Create your models here.



class Sangpum(models.Model):
    sang_id = models.AutoField(primary_key=True)
    sang_val = models.IntegerField(max_length=10)
    sang_name = models.CharField(max_length=10)
    sang_pay  = models.CharField(max_length=10)
    sang_stock = models.CharField(max_length=10)
    sang_explain = models.CharField(max_length=100)
    
    
    

class Sangpum2(models.Model):
    sang_id = models.AutoField(primary_key=True)
    sang_val = models.IntegerField(max_length=10)
    sang_name = models.CharField(max_length=10)
    sang_pay  = models.CharField(max_length=10)
    sang_stock = models.CharField(max_length=10)
    sang_explain = models.CharField(max_length=100)
  
    
        