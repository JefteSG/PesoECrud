import datetime
from django.db import models
from .cpf import CPF
from django.core.exceptions import ValidationError


# Create your models here.
class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True)
    sexo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)
    peso = models.FloatField()
    altura = models.FloatField()

    def clean(self): 
        cpf = CPF(self.cpf)
        if not cpf.validate():
            raise ValidationError({'cpf': 'CPF inválido'}) 
        
        if self.sexo not in ['M', 'F']:
            raise ValidationError({'sexo': 'Sexo deve ser "M" ou "F"'})


    
    def calcular_peso_ideal(self):

        if self.sexo == 'M':
            return (72.7 * self.altura) - 58
        
        if self.sexo == 'F':
            return (62.1 * self.altura) - 44.7
        
        raise ValueError('O sexo informado não é válido')