from django.db import models
from uuid import uuid4

from django.db.models.fields.related import ForeignKey

# Create your models here.


class sobrevivente(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
     nome = models.CharField(max_length=50)
     idade = models.PositiveSmallIntegerField()
     HOMEM = 'H'
     MULHER = 'M'
     OUTRO = 'O'
     SEXO_CHOICES = [
        (HOMEM, "Homem"),
        (MULHER, "Mulher"),
        (OUTRO, "Outro")
        ]
     sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
     ultima_latitude = models.DecimalField(max_digits=8,decimal_places=6)
     ultima_longitude =  models.DecimalField(max_digits=9,decimal_places=6)

    # Um sobrevivente deve ter um nome, idade, sexo e último local (latitude,
    # longitude).
    # Um sobrevivente também possui um inventário de recursos de sua própria
    # propriedade (que você precisa declarar quando do registro do sobrevivente).

class inventario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_sobrevivente = models.ForeignKey('sobrevivente', on_delete=models.CASCADE)
    item = models.CharField(max_length=15)
    quantidade_item = models.PositiveIntegerField()