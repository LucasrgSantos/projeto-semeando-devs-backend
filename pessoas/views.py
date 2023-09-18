#from attr import field
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from pessoas.models import Pessoas, Respostas, Valores

#Serializers

class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        # campos que queremos serializar
        fields = ('id', 'nome', 'cpf', 'dataNascimento', 'uf', 'cidade', 'email', 'telefone')

class RespostasSerializer(serializers.ModelSerializer):
    pessoa = serializers.PrimaryKeyRelatedField(queryset=Pessoas.objects.all())

    class Meta:
        model = Respostas
        # campos que queremos serializar
        fields = ('id', 'pessoa', 'resposta1', 'resposta2', 'resposta3', 'resposta4')

class ValoresSerializer(serializers.ModelSerializer):
    pessoa = serializers.PrimaryKeyRelatedField(queryset=Pessoas.objects.all())

    class Meta:
        model = Valores
        # campos que queremos serializar
        fields = ('id', 'pessoa','valorCorrida', 'valorCorridaComDesconto')

#View's

class PessoasView(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all() # filtra todas as pessoas
    serializer_class = PessoasSerializer # classe de serializer que será usada  
    http_method_names = ['get', 'post', 'put', 'delete']  # métodos http permitidos

    def create(self, request, *args, **kwargs):
        # Verificar se já existe uma pessoa com o mesmo CPF
        cpf = request.data.get('cpf')
        if Pessoas.objects.filter(cpf=cpf).exists():
            return Response({'error': 'Já existe uma pessoa com esse CPF.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def verificar_cpf_duplicado(self, request, cpf):
        # Consulte o banco de dados para verificar se o CPF já está cadastrado
        is_duplicado = Pessoas.objects.filter(cpf=cpf).exists()
        return JsonResponse({'is_duplicado': is_duplicado})

class RespostasView(viewsets.ModelViewSet):
    queryset = Respostas.objects.all() # filtra todas as resposstas
    serializer_class = RespostasSerializer # classe de serializer que será usada  
    http_method_names = ['get', 'post', 'put', 'delete']  # métodos http permitidos

class ValoresView(viewsets.ModelViewSet):
    queryset = Valores.objects.all() # filtra todas as resposstas
    serializer_class = ValoresSerializer # classe de serializer que será usada  
    http_method_names = ['get', 'post', 'put', 'delete']  # métodos http permitidos