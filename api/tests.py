from django.test import TestCase
from .cpf import CPF
from .service import Service
from .task import Task
from .models import Pessoa 


class TestService(TestCase):
    def setUp(self):
        self.service = Service
        self.pessoa = Pessoa.objects.create(
            nome='Jefte Sales Gonçalves',
            data_nascimento='1997-08-22',
            sexo='M',
            cpf='28987839001',
            peso=80,
            altura=1.80
        )

    def test_incluir(self):
        data = {
            'nome': 'Fulano de Tal',
            'data_nascimento': '1980-05-10',
            'sexo': 'M',
            'cpf': '40888833052',  # CPF válido
            'peso': 70,
            'altura': 1.75
        }
        self.pessoa_criada = self.service.incluir(data)
        self.assertTrue(Pessoa.objects.filter(cpf='40888833052').exists())

    def test_incluir_cpf_invalido(self):
        data = {
            'nome': 'Ciclano de Tal',
            'data_nascimento': '1985-11-15',
            'sexo': 'M',
            'cpf': '12345678900',  # CPF inválido
            'peso': 75,
            'altura': 1.70
        }
        with self.assertRaises(ValueError):
            self.service.incluir(data)

    def test_alterar(self):
        data = {
            'id': self.pessoa.id,
            'nome': 'Rodrigo Sales Gonçalves',
            'data_nascimento': '1997-08-25',
            'sexo': 'M',
            'cpf': '28987839001', 
            'peso': 82,
            'altura': 1.82
        }
        self.service.alterar(data)
        pessoa = Pessoa.objects.get(id=self.pessoa.id)
        self.assertEqual(pessoa.nome, 'Rodrigo Sales Gonçalves')
        self.assertEqual(pessoa.peso, 82)

    def test_pesquisar_id(self):
        data = {'id': self.pessoa.id}
        pessoa_encontrada = self.service.pesquisar(data)
        self.assertEqual(pessoa_encontrada.peso, 80)

    def test_pesquisar_todos(self):
        pessoas_encontradas = self.service.pesquisar({})
        self.assertEqual(len(pessoas_encontradas), 1)

    def test_excluir(self):
        data = {'id': self.pessoa.id}
        self.service.excluir(data)
        self.assertFalse(Pessoa.objects.filter(id=self.pessoa.id).exists())


class TestCPF(TestCase):
    def setUp(self):
        self.cpf = CPF('28987839001')

    def test_cpf_valido(self):
        self.assertTrue(self.cpf.validate())

    def test_cpf_invalido(self):
        self.cpf = CPF('28987839002')
        self.assertFalse(self.cpf.validate())

    def test_format(self):
        self.assertEqual(self.cpf.format(), '289.878.390-01')
