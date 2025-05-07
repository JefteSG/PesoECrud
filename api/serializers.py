from rest_framework import serializers
from .models import Pessoa

class DTOPessoa(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = "__all__"

        
    # def create(self, validated_data):
    #     return Pessoa.objects.create(**validated_data)
    
