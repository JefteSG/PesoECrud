from rest_framework.test import APITestCase
from django.test import TestCase
from rest_framework import status
from .models import Pessoa
from .cpf import CPF

class TestPessoaAPI(APITestCase):
    def setUp(self):
        self.pessoa = Pessoa.objects.create(
            nome='Jefte Sales Gonçalves',
            data_nascimento='1997-08-22',
            sexo='M',
            cpf='28987839001',
            peso=80,
            altura=1.80
        )

    def test_create_pessoa(self):
        data = {
            'nome': 'Fulano de Tal',
            'data_nascimento': '1980-05-10',
            'sexo': 'M',
            'cpf': '11144477735',  # CPF válido
            'peso': 70,
            'altura': 1.75
        }
        response = self.client.post('/api/v1/pessoa/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Pessoa.objects.filter(cpf='11144477735').exists())

    def test_create_pessoa_cpf_invalido(self):
        data = {
            'nome': 'Ciclano de Tal',
            'data_nascimento': '1985-11-15',
            'sexo': 'M',
            'cpf': '12345678900',  # CPF inválido
            'peso': 75,
            'altura': 1.70
        }
        response = self.client.post('/api/v1/pessoa/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_pessoa(self):
        data = {
            'nome': 'Rodrigo Sales Gonçalves',
            'data_nascimento': '1997-08-25',
            'sexo': 'M',
            'cpf': '28987839001', 
            'peso': 82,
            'altura': 1.82
        }
        response = self.client.put(f'/api/v1/pessoa/{self.pessoa.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pessoa.refresh_from_db()
        self.assertEqual(self.pessoa.peso, 82)

    def test_retrieve_pessoa(self):
        response = self.client.get(f'/api/v1/pessoa/{self.pessoa.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['peso'], 80)

    def test_list_pessoas(self):
        response = self.client.get('/api/v1/pessoa/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_pessoa(self):
        response = self.client.delete(f'/api/v1/pessoa/{self.pessoa.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
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