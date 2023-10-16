from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class User(AbstractUser):
    name = models.TextField(default = '')
    description = models.TextField(default = '')
    quantity = models.PositiveIntegerField(default = 0, validators = [MinValueValidator(0),MaxValueValidator(100)])
 
 