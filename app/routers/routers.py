from typing import Any, Dict

from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter

from app.database.database import db
from app.graphql.schema import schema


async def get_context(session: Session = Depends(db.get_db)) -> Dict[str, Any]:
    return {
        'db': session,
        # Você pode adicionar outras coisas ao contexto aqui, como usuário logado
    }


graphql_app = GraphQLRouter(schema, context_getter=get_context)
