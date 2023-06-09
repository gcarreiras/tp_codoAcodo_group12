from django.db import models

#from tasks.models import User para hacer la importacion en el shell IMPORTANTE

# Create your models here.

# Relacion 1 a n entre User y Accessory -> Un usuario con n accesorios

class User(models.Model):
     username = models.CharField(max_length=50, verbose_name='Username')
     password = models.CharField(max_length=50, verbose_name='Password')

##### marca a productos y productos a marcas 

class Brand(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Accessory brand')
    accessories = models.ManyToManyField('Accessory', verbose_name='Accessories', related_name='brand_set')

    def __str__(self):
          return (f"{self.brand}")

class Accessory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Accessory name')
    color = models.CharField(max_length=50, verbose_name='Accessory color')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brand', related_name='accessory_set')
    description = models.CharField(max_length=100, verbose_name='Accessory description')
    image = models.FileField(verbose_name='Accessory image', null=True)
    price = models.FloatField(verbose_name='Accessory price')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, related_name='accessories')

    def __str__(self):
          return (f"Nombre: {self.name}")