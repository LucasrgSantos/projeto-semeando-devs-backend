from rest_framework import serializers
from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status

from taxistas.models import Taxista

class TaxistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxista

        fields = ('id', 'nome', 'cpf', 'numero')

class TaxistaView(viewsets.ModelViewSet):
    queryset = Taxista.objects.all()
    serializer_class = TaxistaSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

