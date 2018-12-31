from django.db import models

class Utilisateur(models.Model) :
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=50)