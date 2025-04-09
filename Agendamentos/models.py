from django.db import models
from django.contrib.auth.models import User
from Service.models import servico


class agenda(models.Model):
    cliente = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='agendaUsuario')
    data = models.DateField()
    hora = models.TimeField()
    service = models.ForeignKey(
        servico, on_delete=models.PROTECT, related_name='servicoUsuario')

    def __str__(self):
        return self.service
