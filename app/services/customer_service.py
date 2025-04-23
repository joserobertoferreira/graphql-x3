# # app/services/customer_service.py
# from sqlalchemy.orm import Session
# from sqlalchemy.exc import IntegrityError

# # Importe seus modelos SQLAlchemy
# from app.models.customer import Customer
# from app.models.address import Address

# # Importe seus tipos de Input (Pydantic ou Strawberry Inputs convertidos)
# # Supondo que você tenha Pydantic models para entrada de dados na API
# # Se usar Strawberry Inputs direto, a assinatura do método muda um pouco.
# from app.schemas.customer import CustomerCreateSchema # Exemplo com Pydantic
# from app.schemas.address import AddressCreateSchema   # Exemplo com Pydantic

# class CustomerService:
#     def __init__(self, db: Session):
#         """
#         Injeta a sessão do banco de dados.
#         FastAPI/Strawberry podem injetar isso automaticamente usando Depends.
#         """
#         self.db = db

#     def create_customer_with_address(
#         self,
#         customer_data: CustomerCreateSchema,
#         address_data: AddressCreateSchema
#     ) -> Customer:
#         """
#         Cria um cliente e seu endereço principal atomicamente.
#         Realiza validações de negócio (exemplo simples).
#         """
#         # 1. Validação de Negócio (Exemplo)
#         if not customer_data.customer_name: # Exemplo de validação simples
#             raise ValueError("Nome do cliente não pode ser vazio.")
#         if self.db.query(Customer).filter(Customer.customer_number == customer_data.customer_number).first():
#             raise ValueError(f"Cliente com número {customer_data.customer_number} já existe.")
#         if not address_data.address_line_1 or not address_data.city or not address_data.country_code:
#              raise ValueError("Endereço principal incompleto.")

#         # 2. Criação das Instâncias dos Modelos SQLAlchemy
#         # Assumindo que Address tem um campo `is_primary` ou similar
#         # e Customer tem um relacionamento `addresses` e talvez `primary_address_id`
#         new_address = Address(
#             **address_data.model_dump(),
#             # bpa_number=customer_data.customer_number, # Pode ser necessário linkar
#             # is_primary=True # Exemplo de campo para indicar endereço principal
#         )

#         new_customer = Customer(
#             **customer_data.model_dump(),
#             # Você pode querer associar o endereço aqui se o relacionamento permitir
#             # Ex: primary_address = new_address (depende da definição do relationship)
#         )

#         # Se o relacionamento for via FK no endereço:
#         new_address.customer = new_customer # Associa antes de adicionar à sessão se a FK estiver no endereço

#         # 3. Operação de Banco de Dados
#         try:
#             self.db.add(new_address)
#             self.db.add(new_customer)
#             # Se a FK estiver no cliente e precisar do ID do endereço:
#             # self.db.flush() # Obtém o ID do endereço antes de associar ao cliente
#             # new_customer.primary_address_id = new_address.row_id
#             # self.db.add(new_customer) # Adiciona o cliente atualizado

#             self.db.commit()
#             self.db.refresh(new_customer)
#             self.db.refresh(new_address) # Garante que temos todos os dados do DB

#             # Carregar o relacionamento se necessário para o retorno
#             # (pode ser feito no resolver também com loader options)
#             # self.db.query(Customer).options(joinedload(Customer.primary_address)).filter(Customer.row_id == new_customer.row_id).first()

#         except IntegrityError as e:
#             self.db.rollback()
#             # Log do erro e/ou levanta uma exceção mais específica de negócio
#             print(f"Erro de integridade ao criar cliente/endereço: {e}")
#             raise ValueError("Erro ao salvar os dados. Verifique os valores únicos.") from e
#         except Exception as e:
#             self.db.rollback()
#             print(f"Erro inesperado: {e}")
#             raise RuntimeError("Ocorreu um erro interno ao criar o cliente.") from e

#         # 4. Retorno (opcionalmente pode retornar um DTO/Schema Pydantic também)
#         return new_customer

#     def get_customer_details(self, customer_number: str) -> Customer | None:
#         """Busca um cliente com detalhes (ex: endereço principal)."""
#         # Aqui você pode adicionar lógica para carregar relacionamentos
#         # ou fazer queries mais complexas que não cabem diretamente no modelo.
#         # Ex: usar joinedload ou selectinload para otimizar a busca de relacionamentos
#         from sqlalchemy.orm import joinedload

#         customer = self.db.query(Customer)\
#             .options(joinedload(Customer.addresses)) # Exemplo de eager loading
#             .filter(Customer.customer_number == customer_number)\
#             .first()
#         return customer

#     # ... outros métodos de serviço para Customer ...
#     # ex: update_customer_status, calculate_customer_lifetime_value, etc.
