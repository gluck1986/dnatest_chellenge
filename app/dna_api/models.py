# Create your models here.
from django.db import models


class Dna(models.Model):
    animal_name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    test_date = models.DateField(blank=False)
    milk_yield = models.FloatField()
    health_status = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.animal_name
