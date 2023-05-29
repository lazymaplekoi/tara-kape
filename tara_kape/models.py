from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    phone_number = models.CharField(max_length=20)
    website = models.URLField()
    has_wifi = models.BooleanField()
    has_sockets = models.BooleanField()
    has_comfortable_tables = models.BooleanField()
    work_hours = models.TextField()