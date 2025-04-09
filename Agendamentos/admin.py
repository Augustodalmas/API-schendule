from django.contrib import admin
from Agendamentos.models import agenda


@admin.register(agenda)
class adminAgenda(admin.ModelAdmin):
    list_display = ('data', 'hora')
