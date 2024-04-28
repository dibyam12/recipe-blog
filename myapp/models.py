from django.db import models

# Create your models here.
""" 
class Menu(models.Model):
    name = models.CharField(max_length=30)
    
class MenuItem(models.Model):
    name= models.CharField(max_length=80)
    category = models.CharField(max_length=30)
    price= models.FloatField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
 """
