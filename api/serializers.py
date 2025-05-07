from rest_framework import serializers
from .models import Pessoa


class DTOPessoa(serializers.Serializer):
    class Meta:
        fields = ('id', 'nome', 'data_nascimento', 'sexo', 'cpf', 'peso', 'altura')
        model = Pessoa


    def create(self, validated_data):
        return Pessoa.objects.create(**validated_data)
    