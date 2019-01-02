from django.db import models

# Create your models here.

class Utilisateur(models.Model) :
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    email = models.EmailField()
