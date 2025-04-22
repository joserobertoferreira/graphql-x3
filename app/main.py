from fastapi import FastAPI

# from sqlalchemy import select

# from .database import engine
# from .models import ExemploTabela

app = FastAPI()


# @app.get('/exemplo/')
# async def get_exemplo():
#     with engine.connect() as connection:
#         result = connection.execute(select(ExemploTabela))
#         exemplos = [{'id': row.id, 'nome': row.nome, 'descricao': row.descricao} for row in result]
#     return exemplos
