from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Pessoa
from .serializers import DTOPessoa


class PessoaViewSet(viewsets.ModelViewSet):
    """
    Um ViewSet para visualizar, criar, editar e excluir registros de Pessoas.

    Fornece as operações padrão de CRUD, além de um endpoint customizado
    para o cálculo do peso ideal.
    """
    queryset = Pessoa.objects.all()
    serializer_class = DTOPessoa

    def create(self, request, *args, **kwargs):
        """
        Cria um novo registro de pessoa.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retorna os detalhes de um registro de pessoa específico.
        """
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        Retorna uma lista de todos os registros de pessoas.
        """
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Atualiza completamente um registro de pessoa existente.
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Atualiza parcialmente um registro de pessoa existente.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Exclui um registro de pessoa existente.
        """
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['get'], url_path='peso-ideal')
    def peso_ideal(self, request, pk=None):
        """
        Calcula e retorna o peso ideal para a pessoa especificada.

        A fórmula utilizada é:
        - **Homens:** (72.7 * altura) - 58
        - **Mulheres:** (62.1 * altura) - 44.7
        """
        pessoa = self.get_object()  # Retorna 404 Not Found automaticamente se não existir
        peso_ideal_valor = pessoa.calcular_peso_ideal()
        return Response({'peso_ideal': peso_ideal_valor})