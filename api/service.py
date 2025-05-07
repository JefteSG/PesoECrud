from .task import Task


class Service:
    @staticmethod
    def incluir(data):
        try:
            print(data)
            Task.incluir(data)
        except Exception as e:
            raise e

    @staticmethod
    def alterar(data):
        try:
            Task.alterar(data)
        except Exception as e:
            raise e

    @staticmethod
    def excluir(data):
        try:
            Task.excluir(data)
        except Exception as e:
            raise e

    @staticmethod
    def pesquisar(data):
        return Task.pesquisar(data)
    

    @staticmethod
    def calcular_peso_ideal(data):
        try:
            return Task.calcular_peso_ideal(data)
        except Exception as e:
            raise e
    