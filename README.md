# API GraphQL X3

```
api/
├── app/                   # Código principal da aplicação
│   ├── __init__.py
│   ├── main.py            # Instância FastAPI, roteador principal GraphQL
│   ├── core/              # Configurações, dependências centrais
│   │   ├── __init__.py
│   │   └── settings.py    # Leitura de variáveis de ambiente, etc.
│   ├── database/          # Camada de acesso ao banco de dados
│   │   ├── __init__.py
│   │   ├── base.py        # Definição da Base declarativa (DeclarativeBase)
│   │   └── database.py    # Lógica de sessão (engine, SessionLocal, get_db dependency)
│   ├── models/            # Modelos SQLAlchemy (representação do DB)
│   │   ├── __init__.py    # Pode exportar todos os modelos para facilitar imports
│   │   ├── address.py     # Ex: class Address(Base): ... (mapear BPADDRESS)
│   │   ├── customer.py    # Ex: class Customer(Base): ... (mapear BPCUSTOMER)
│   │   └── ...            # Outros modelos
│   ├── graphql/           # Tudo relacionado ao GraphQL (API Layer)
│   │   ├── __init__.py
│   │   ├── schema.py      # Definição principal do strawberry.Schema(query=Query, mutation=Mutation)
│   │   ├── types/         # Definições de tipos Strawberry (@strawberry.type)
│   │   │   ├── __init__.py
│   │   │   ├── address.py # Ex: @strawberry.type class AddressType: ...
│   │   │   ├── customer.py# Ex: @strawberry.type class CustomerType: ...
│   │   │   └── ...        # Outros tipos
│   │   ├── queries/       # Definições parciais da Query (agrupadas por funcionalidade)
│   │   │   ├── __init__.py
│   │   │   ├── address.py # Ex: class AddressQuery: @strawberry.field def address(...)
│   │   │   └── customer.py# Ex: class CustomerQuery: @strawberry.field def customer(...)
│   │   ├── mutations/     # Definições parciais da Mutation (agrupadas por funcionalidade)
│   │   │   ├── __init__.py
│   │   │   ├── address.py # Ex: class AddressMutation: @strawberry.mutation def createAddress(...)
│   │   │   └── customer.py# Ex: class CustomerMutation: @strawberry.mutation def updateCustomer(...)
│   │   └── resolvers/     # Opcional: Lógica de resolver complexa separada (embora Strawberry incentive resolvers como métodos)
│   ├── api/               # Autenticação (API REST)
│   │   ├── __init__.py
│   │   └── routers/
│   └── services/          # Opcional: Camada de lógica de negócio (se complexa)
│       ├── __init__.py
│       └── ...
├── .env                   # Variáveis de ambiente (NÃO versionar)
├── .gitignore
├── pyproject.toml         # Definições de projeto
├── requirements.txt       # dependências de projeto
├── requirements-dev.txt   # dependências de desenvolvimento
└── README.md
```
