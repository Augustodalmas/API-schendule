from Service.models import servico
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = servico
        fields = "__all__"
