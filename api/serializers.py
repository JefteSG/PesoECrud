from rest_framework import serializers
from .models import Pessoa
from .cpf import CPF

class DTOPessoa(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = "__all__"

    def validate_cpf(self, value):
        cpf = CPF(value)
        if not cpf.validate():
            raise serializers.ValidationError("CPF inválido.")
        return value

    def validate_sexo(self, value):
        if value.upper() not in ['M', 'F']:
            raise serializers.ValidationError('Sexo deve ser "M" ou "F".')
        return value.upper()

    
