from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    Category = models.CharField(max_length=100,null=True,blank=True)
    Category_Image = models.ImageField(upload_to="Categories",null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)

class ProductDb(models.Model):
    Product_Category = models.CharField(max_length=100,null=True,blank=True)
    Product_Name = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    MRP = models.IntegerField(null=True,blank=True)
    Description = models.TextField(max_length=300,null=True,blank=True)
    Country = models.CharField(max_length=100,null=True,blank=True)
    Manufactured = models.CharField(max_length=100,null=True,blank=True)
    Image1 = models.ImageField(upload_to="Products",null=True,blank=True)
    Image2 = models.ImageField(upload_to="Products", null=True, blank=True)
    Image3 = models.ImageField(upload_to="Products", null=True, blank=True)