from Agendamentos.models import agenda
from rest_framework import generics
from Agendamentos.serializer import AgendaSerializer


class agendaCriarListarView(generics.ListCreateAPIView):
    queryset = agenda.objects.all().order_by('data')
    serializer_class = AgendaSerializer


class agendaAtualizarDeleterView(generics.RetrieveUpdateDestroyAPIView):
    queryset = agenda.objects.all()
    serializer_class = AgendaSerializer
