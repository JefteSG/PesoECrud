# Projeto Django - Sistema de Cadastro de Pessoas

Este projeto consiste em uma API RESTful desenvolvida com Django e PostgreSQL, com uma interface web separada HTML5 para gerenciar cadastros de pessoas. A aplicação permite incluir, alterar, excluir e pesquisar registros de pessoas, além de calcular o peso ideal com base na altura e sexo do usuário.

## 🔧 Tecnologias Utilizadas

- **Backend**: Django (Python)
- **Frontend**: HTML5
- **Banco de Dados**: PostgreSQL
- **Documentação de API**: Swagger (drf-yasg)
- **Testes**: Django TestCase (unitários e de integração)
- **ORM**: Django ORM
## 🔧 Swagger

<img href="https://github.com/JefteSG/ImcECrud/blob/main/assets/swagger.png">

## 📁 Estrutura do Projeto
```plaintext
peso_ideal_api/
├── pessoa/
│   ├── migrations/
│   ├── models.py         # Model Pessoa
│   ├── serializers.py    # DTO
│   ├── services.py       # Camada de serviço
│   ├── tasks.py          # Camada de Lógica
│   ├── views.py          # Controllers (REST)
│   └── tests.py          # Testes automatizados
├── peso_ideal_api/
│   ├── settings.py
│   ├── urls.py           # Inclui Swagger e rotas da API
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## 📌 Requisitos da Prova

### Funcionalidades
- [x] CRUD completo da entidade Pessoa
- [x] Chamada REST via JSON
- [x] Interface Web (HTML5 separada do backend)
- [x] Lógica em camadas: Controller → Service → Task
- [x] DTO com persistência via ORM
- [x] Swagger para documentação da API
- [x] Testes automatizados
- [x] Cálculo de peso ideal com popup

### Fórmula do Peso Ideal:
Para homens = (72.7 * altura) - 58

Para mulheres = (62.1 * altura) - 44.7


## ⚙️ Instalação e Execução

### Pré-requisitos
- Docker
- Docker-compose

### Passos

```bash
# Clone o projeto
git clone git@github.com:JefteSG/PesoECrud.git peso_ideal_api
cd peso_ideal_api

docker-compose up --build
```
Acesse a interface Swagger em:
👉 http://localhost:8010/docs/

🔍 Endpoints Principais


| Método | Endpoint                    | Descrição                  |
|--------|-----------------------------|----------------------------|
| POST   | /api/pessoa/                | Criar nova pessoa          |
| PUT    | /api/pessoa/&lt;id&gt;/           | Alterar pessoa existente   |
| DELETE | /api/pessoa/&lt;id&gt;/           | Excluir pessoa             |
| GET    | /api/pessoa/                | Pesquisar todas pessoas    |
| GET    | /api/pessoa/&lt;id&gt;/peso-ideal/| Calcular peso ideal        |

🧪 Testes
Para rodar os testes:

python manage.py test
Os testes cobrem:

Criação, alteração, exclusão e listagem de pessoas

Validação da fórmula de peso ideal

Verificação de respostas HTTP e integridade do banco

🧑‍💻 Interface Cliente
A interface é feita com HTML5. O frontend comunica-se com o backend via chamadas REST em JSON. O botão de "Calcular Peso Ideal" envia um GET ao backend e exibe o resultado em uma popup/modal.