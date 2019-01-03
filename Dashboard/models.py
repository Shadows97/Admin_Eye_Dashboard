from django.db import models

# Create your models here.

class Utilisateur(models.Model) :
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    email = models.EmailField()


class Moniteur(models.Model):
    nom = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)

class Equipement(models.Model) :
    nom = models.CharField(max_length=50)
    adress_ip = models.CharField(max_length=50)
    adress_mac = models.CharField(max_length=50)
    etat = models.BooleanField(default=False)


