from django.db import models

# Create your models here.
class User(models.Model):
     username = models.CharField(max_length=50, verbose_name='Username')
     password = models.CharField(max_length=50, verbose_name='Password')

class Accesory(models.Model):
     name = models.CharField(max_length=20, verbose_name='Accesory name')
     color = models.CharField(max_length=20, verbose_name='Accesory name')
     brand = models.CharField(max_length=20, verbose_name='Accesory name')
     color = models.CharField(max_length=20, verbose_name='Accesory name')
     description = models.CharField(max_length=20, verbose_name='Accesory name')
     image = models.FileField()
     price = models.FloatField()