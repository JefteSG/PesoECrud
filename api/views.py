from .models import Pessoa
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import DTOPessoa
# from .models import Pessoa
from rest_framework.decorators import action
from .service import Service
# Create your views here.


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = DTOPessoa

    @action(methods=['get'], detail=False)
    def pesquisar(self, request):
        data = request.query_params.dict()
        pessoas = Service.pesquisar(data)
        if not isinstance(pessoas, Pessoa):
            serializer = DTOPessoa(pessoas, many=True)
        else:
            serializer = DTOPessoa(pessoas)

        return Response(serializer.data)


    @action(methods=['post'], detail=False)
    def incluir(self, request):
        data = request.data
        try:
            pessoa = Service.incluir(data)
            serializer = DTOPessoa(instance=pessoa)
            print(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    

    @action(methods=['put'], detail=False)
    def alterar(self, request):
        data = request.data
        pessoa = None
        try:
            pessoa = Service.alterar(data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        serializer = DTOPessoa(pessoa)
        return Response(serializer.data)


    @action(methods=['delete'], detail=False)
    def excluir(self, request):
        data = request.data
        try:
            Service.excluir(data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    @action(methods=['post'], detail=False)
    def calcular_peso_ideal(self, request):
        data = request.data
        peso_ideal = None
        print(data)
        if not data.get('id'):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            peso_ideal = Service.calcular_peso_ideal(data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
        return Response(peso_ideal, status=status.HTTP_200_OK)