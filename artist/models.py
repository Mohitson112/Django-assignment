from django.db import models
from work.models import *

class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField(WorkDetail)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
