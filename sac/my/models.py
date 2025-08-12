from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
# id is created as aan auto feild
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField()
    
    def __str__(self):
        return self.name



