from django.db import models

class CarCount(models.Model):
    year = models.IntegerField()
    count = models.IntegerField()

class CompanyWiseCarCount(models.Model):
    CompanyName = models.CharField(max_length=100)
    eleven = models.IntegerField()
    twelve = models.IntegerField()
    thirteen = models.IntegerField()

class Mileage(models.Model):
    company = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=15)
    costfor25 = models.CharField(max_length=10)
    annualcost = models.CharField(max_length=10)

