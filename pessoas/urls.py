from django.urls import path, include
from . import views
from rest_framework import routers

from pessoas.views import PessoasView, RespostasView, ValoresView

router = routers.DefaultRouter()
router.register('pessoas', PessoasView) # nome do objeto da view
router.register('respostas', RespostasView)
router.register('valores', ValoresView)

urlpatterns = [
    path('pessoas/', include(router.urls)), #nome do app
    path('verificar-cpf-duplicado/<str:cpf>/', PessoasView.as_view({'get': 'verificar_cpf_duplicado'}), name='verificar_cpf_duplicado')
]