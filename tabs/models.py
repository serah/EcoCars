from django.db import models

class CarCount(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    count = models.IntegerField()

class CompanyWiseCarCount(models.Model):
    id = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=100)
    eleven = models.IntegerField()
    twelve = models.IntegerField()
    thirteen = models.IntegerField()

class Mileage(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=15)
    costfor25 = models.CharField(max_length=10)
    annualcost = models.CharField(max_length=10)

class GasRate(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=50)
    price = models.FloatField()

class GasolineCarCount(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    count = models.BigIntegerField()

class GrowthPerYear(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    count = models.BigIntegerField()

class ElectricitySources(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=50)
    percentage = models.FloatField()
