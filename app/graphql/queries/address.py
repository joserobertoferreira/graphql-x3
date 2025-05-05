from typing import List

import strawberry
from sqlalchemy import select
from sqlalchemy.orm import Session
from strawberry.types import Info

from app.graphql.types.address import Address as AddressType
from app.middleware.auth.permissions import IsAuthenticated
from app.models.address import Address as AddressModel

ContextType = dict


@strawberry.type
class AddressQuery:
    @strawberry.field(permission_classes=[IsAuthenticated])
    def addresses_by_entity(  # noqa: PLR6301
        self, info: Info[ContextType, None], entity_number: str
    ) -> List[AddressType]:
        """Busca todos os endereços associados a um número de entidade."""
        db: Session = info.context['db']

        stmt = select(AddressModel).where(AddressModel.entityNumber == entity_number)

        result = db.execute(stmt)

        db_addresses = result.scalars().all()

        if not db_addresses:
            return []

        return db_addresses
