from django.db import models

class Listing(models.Model):
    phone_number = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    currency = models.CharField(max_length=5)
    action = models.CharField(max_length=10)
    at = models.FloatField()#rate
    pair = models.CharField(max_length=5)