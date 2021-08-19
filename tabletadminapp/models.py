from django.db import models
import datetime

# Create your models here.

class Nap(models.Model):
    ev=models.IntegerField()
    ho=models.IntegerField()
    nap=models.IntegerField()

    def __str__(self):
        return str(".".join([str(self.ev),str(self.ho),str(self.nap)]))

class Foglalas(models.Model):
    id=models.AutoField(primary_key=True)
    tanar=models.CharField(max_length=64,default="test")
    oraszam = models.IntegerField()
    mennyiseg = models.IntegerField()
    nap = models.ForeignKey(Nap,on_delete=models.CASCADE)

class Kornyezeti(models.Model):
    alap=models.IntegerField(default=1)
    elerhetotablet=models.IntegerField()
    napioraszam=models.IntegerField()