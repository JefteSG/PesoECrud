import datetime
from django.db import models
from .cpf import CPF

# Create your models here.
class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True)
    sexo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)
    peso = models.FloatField(default=None, null=True)
    altura = models.FloatField(default=None, null=True)

    def clean(self):
        try:
            datetime.strptime(self.data_nascimento, "%Y-%m-%d")
        except ValueError:
            raise ValueError("VALOR DE DATA INVÁLIDO")
        
        cpf = CPF(self.cpf)
        if not cpf.validate():
            raise ValueError('O CPF informado não é válido') 
        
    
    def calcular_peso_ideal(self):

        if self.sexo == 'M':
            return (72.7 * self.altura) - 58
        
        if self.sexo == 'F':
            return (62.1 * self.altura) - 44.7
        
        raise ValueError('O sexo informado não é válido')