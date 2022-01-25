from django.db import models
from django.urls import reverse

# Create your models here.
#model for beer
class Beer(models.Model):
    name=models.CharField(max_length=150)
    taste=models.CharField(max_length=150)
    color=models.CharField(max_length=150)
    price = models.FloatField();

    def __str__(self):
        return self.name
