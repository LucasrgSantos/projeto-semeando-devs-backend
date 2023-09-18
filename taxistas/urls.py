from django.urls import path, include
from rest_framework import routers

from taxistas.views import TaxistaView
from .validar_numero_taxista import validar_numero_taxista



router = routers.DefaultRouter()
router.register('taxistas', TaxistaView)  # nome do objeto da view

urlpatterns = [
    path('taxistas/', include(router.urls)),  # nome do app
    path('validar_numero_taxista/', validar_numero_taxista, name='validar_numero_taxista'),
]
