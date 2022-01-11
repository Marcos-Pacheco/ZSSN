from django.db.models import fields
from rest_framework import serializers
from sobreviventes import models

class sobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.sobrevivente
        fields = '__all__'

class inventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.inventario
        fields = '__all__'