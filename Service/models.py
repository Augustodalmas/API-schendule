from django.db import models


class servico(models.Model):
    nome = models.CharField(max_length=256)
    preco = models.FloatField()

    def __str__(self):
        return self.nome
