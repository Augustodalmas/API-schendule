from Agendamentos.models import agenda
from rest_framework import serializers


class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = agenda
        fields = "__all__"

    def validate(self, data):

        data_agendamento = data.get('data')
        print(data_agendamento)
        hora_agendamento = data.get('hora')
        print(hora_agendamento)

        if agenda.objects.filter(data=data_agendamento, hora=hora_agendamento).exists():
            raise serializers.ValidationError(
                "Já existe um serviço nesse horário e data!"
            )

        return data
