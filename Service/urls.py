from django.urls import path
from Service.views import servicoCriarListarView, servicoAtualizarDeleterView

urlpatterns = [
    path('servico', servicoCriarListarView.as_view(),
         name='criar_listar_servico'),
    path('servico/<int:pk>/', servicoAtualizarDeleterView.as_view(),
         name='atualizar_deletar_servico'),
]
