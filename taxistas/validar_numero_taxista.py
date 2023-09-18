from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from taxistas.models import Taxista

@api_view(['POST'])
def validar_numero_taxista(request):
    numero_taxista = request.data.get('numero', None)
    if numero_taxista:
        try:
            taxista = Taxista.objects.get(numero=numero_taxista)
            return Response({'valido': True, 'id_taxista': taxista.id, 'nome_taxista': taxista.nome}, status=status.HTTP_200_OK)
        except Taxista.DoesNotExist:
            pass
    
    return Response({'valido': False}, status=status.HTTP_400_BAD_REQUEST)
