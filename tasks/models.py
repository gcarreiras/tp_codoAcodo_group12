from django.db import models

#from tasks.models import User para hacer la importacion en el shell IMPORTANTE

# Create your models here.

# Relacion 1 a n entre User y Accessory -> Un usuario con n accesorios

class User(models.Model):
     username = models.CharField(max_length=50, verbose_name='Username')
     password = models.CharField(max_length=50, verbose_name='Password')

##### marca a productos y productos a marcas 

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
          return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
          return self.name

class Accessory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Accessory name')
    color = models.CharField(max_length=50, verbose_name='Accessory color')
    brands = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brand')
    description = models.CharField(max_length=100, verbose_name='Accessory description')
    image = models.FileField(verbose_name='Accessory image', null=True)
    price = models.FloatField(verbose_name='Accessory price')
    categories = models.ManyToManyField(Category, verbose_name='Categories')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, related_name='accessories')

    def __str__(self):
          return self.name