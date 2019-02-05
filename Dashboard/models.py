from django.db import models

# Create your models here.

class Utilisateur(models.Model) :
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    email = models.EmailField()


class Moniteur(models.Model):
    nom = models.CharField(max_length=50)
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)

class Equipement(models.Model) :
    nom = models.CharField(max_length=50)
    adresse_ip = models.CharField(max_length=50)
    adresse_mac = models.CharField(max_length=50)
    etat = models.BooleanField(default=False)

class Disk_info (models.Model):
    total_size = models.BigIntegerField()
    size_used = models.BigIntegerField()
    size_free = models.BigIntegerField()
    equipement = models.ForeignKey(Equipement,on_delete=models.CASCADE)

class Cpu_info (models.Model):
    cpu_number = models.IntegerField()
    cpu_current_freq = models.DecimalField(max_digits=19,decimal_places=10)
    cpu_min_freq = models.DecimalField(max_digits=19,decimal_places=10)
    cpu_max_freq = models.DecimalField(max_digits=19,decimal_places=10)
    equipement = models.ForeignKey(Equipement,on_delete=models.CASCADE)

class Interface_data_info (models.Model) :
    byte_send = models.BigIntegerField()
    byte_recv = models.BigIntegerField()
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)

class Ram_info (models.Model) :
    ram_total = models.BigIntegerField()
    ram_available = models.BigIntegerField()
    ram_percent = models.BigIntegerField()
    ram_free = models.BigIntegerField()
    ram_used = models.BigIntegerField()
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)

class Alert (models.Model) :
    titre = models.CharField(max_length=20)
    message = models.CharField(max_length=500)
    status = models.BooleanField()
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)

class Historique (models.Model) :
    browser = models.CharField(max_length=20)
    date_connexion = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)




