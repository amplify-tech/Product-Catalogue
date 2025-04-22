from django.db import models

class Product(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    createDate = models.DateField()
    location = models.CharField()
    bedroomCount = models.IntegerField()



