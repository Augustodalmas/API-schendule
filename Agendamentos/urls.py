from django.urls import path
from Agendamentos.views import agendaAtualizarDeleterView, agendaCriarListarView

urlpatterns = [
    path('agenda', agendaCriarListarView.as_view(), name='criar_listar_agenda'),
    path('agenda/<int:pk>/', agendaAtualizarDeleterView.as_view(),
         name='atualizar_deletar_agenda'),
]
