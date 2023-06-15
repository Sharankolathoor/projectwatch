from django.db import models

# Create your models here.
class branddb(models.Model):
    bname=models.CharField(max_length=50,null=True,blank=True)
    bimage=models.ImageField(upload_to="brand",null=True,blank=True)
    desc=models.CharField(max_length=50,null=True,blank=True)
class productdb(models.Model):
    brand=models.CharField(max_length=50,null=True,blank=True)
    pname=models.CharField(max_length=50,null=True,blank=True)
    des=models.CharField(max_length=50,null=True,blank=True)
    pimage = models.ImageField(upload_to="product", null=True, blank=True)
    price=models.CharField(max_length=50,null=True,blank=True)
