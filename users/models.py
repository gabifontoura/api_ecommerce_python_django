from django.db import models
from django.contrib.auth.models import AbstractUser

class Roles(models.TextChoices):
    client = "Cliente"
    seller = "Vendedor"
    admin = "Administrador"

class User(AbstractUser):
        
    class Meta:
        ordering = ["id"]
    
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.client)
    password = models.CharField(max_length=120) 
    email = models.EmailField(unique=True)
