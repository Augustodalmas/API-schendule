from django.contrib import admin
from Service.models import servico


@admin.register(servico)
class adminServico(admin.ModelAdmin):
    list_display = ('nome', 'preco')
