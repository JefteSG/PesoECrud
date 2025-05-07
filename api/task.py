from .models import Pessoa
from .serializers import DTOPessoa
# lasse denominada Task que efetivamente faz o que
# tem que fazer(incluir, alterar, excluir e pesquisar).

class Task:


    @staticmethod
    def incluir(data):
        serializer = DTOPessoa(data=data)
        if serializer.is_valid():
            print('valido')
            return serializer.save()
        
        raise ValueError(serializer.errors)
    

    def alterar(data):
        pessoa = Pessoa.objects.get(id=data.get('id'))
        serializer = DTOPessoa(pessoa, data=data, patial=True)
        if serializer.is_valid():
            return pessoa.save()
        
        raise ValueError(pessoa.errors)
    

    def excluir(data):
        pessoa = None
        try:
            pessoa = Pessoa.objects.get(id=data.get('id'))
        except Pessoa.DoesNotExist:
            raise ValueError('Pessoa não encontrada')
        pessoa.delete()


    def pesquisar(data):
        if data.get('id'):
            return Pessoa.objects.get(id=data.get('id'))
        return Pessoa.objects.all()


    def calcular_peso_ideal(data):
        pessoa = Pessoa.objects.get(id=data.get('id'))
        return pessoa.calcular_peso_ideal()
        