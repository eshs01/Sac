from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
# id is created as aan auto feild
    name = models.CharField(max_length=64)
    discription = models.TextField()
    price = models.FloatField()
    
    def __str__(self):
        return self.name

class cart(models.Model):
    base= models.ForeignKey(product,on_delete=models.CASCADE,related_name="tiltle") 

