from django.db import models

#from tasks.models import User para hacer la importacion en el shell IMPORTANTE

# Create your models here.

# Relacion 1 a n entre User y Accessory -> Un usuario con n accesorios

class User(models.Model):
     username = models.CharField(max_length=50, verbose_name='Username')
     password = models.CharField(max_length=50, verbose_name='Password')

class Accessory(models.Model):
     name = models.CharField(max_length=50, verbose_name='Accesory name')
     color = models.CharField(max_length=50, verbose_name='Accesory color')
     brand = models.CharField(max_length=50, verbose_name='Accesory brand')
     description = models.CharField(max_length=100, verbose_name='Accesory description')
     image = models.FileField(verbose_name='Accesory image')
     price = models.FloatField(verbose_name='Accesory price')
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, related_name='accessories')
     
     def __str__(self):
          return (f"Nombre: {self.name}")