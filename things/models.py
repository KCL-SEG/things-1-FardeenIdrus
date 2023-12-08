from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length= 30, unique = True, blank = False)
    description = models.TextField(max_length= 120, unique= False, blank = True)
    quantity = models.IntegerField(unique = False,
                validators= [
                    MaxValueValidator(100),
                    MinValueValidator(0)
                ]
                )
 
 