from rest_framework import viewsets
from api import serializers
from sobreviventes import models

class sobreviventeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.sobreviventeSerializer
    queryset = models.sobrevivente.objects.all()

# class inventarioViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.inventarioSerializer
#     queryset = models.sobrevivente.objects.all()
