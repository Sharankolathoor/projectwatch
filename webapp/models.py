from django.db import models

# Create your models here.
class registerdb(models.Model):
    username=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)
    profile=models.ImageField(upload_to="register",null=True,blank=True)
class contactdb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    subject=models.CharField(max_length=50,null=True,blank=True)
    message=models.CharField(max_length=50,null=True,blank=True)
class cartdb(models.Model):
    c_username=models.CharField(max_length=50,null=True,blank=True)
    c_pname=models.CharField(max_length=50,null=True,blank=True)
    c_description=models.CharField(max_length=50,null=True,blank=True)
    c_quantity=models.IntegerField(null=True,blank=True)
    c_price=models.IntegerField(null=True,blank=True)
    c_totalprice=models.IntegerField(null=True,blank=True)
    # c_image=models.ImageField(upload_to="cart",null=True,blank=True)
class checkoutdb(models.Model):
    ck_fname=models.CharField(max_length=50,null=True,blank=True)
    ck_lname=models.CharField(max_length=50,null=True,blank=True)
    ck_phone=models.IntegerField(null=True,blank=True)
    ck_email=models.EmailField(max_length=50,null=True,blank=True)
    ck_country=models.CharField(max_length=50,null=True,blank=True)
    ck_address=models.CharField(max_length=50,null=True,blank=True)
    ck_district=models.CharField(max_length=50,null=True,blank=True)
    ck_town=models.CharField(max_length=50,null=True,blank=True)
    ck_pin=models.IntegerField(null=True,blank=True)
