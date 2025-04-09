from Service.models import servico
from rest_framework import generics
from Service.serializer import ServiceSerializer


class servicoCriarListarView(generics.ListCreateAPIView):
    queryset = servico.objects.all()
    serializer_class = ServiceSerializer


class servicoAtualizarDeleterView(generics.RetrieveUpdateDestroyAPIView):
    queryset = servico.objects.all()
    serializer_class = ServiceSerializer
