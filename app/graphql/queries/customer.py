from typing import List, Optional

import strawberry
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from strawberry.types import Info

from app.graphql.types.customer import Customer as CustomerType
from app.middleware.auth.permissions import IsAuthenticated
from app.models.customer import Customer as CustomerModel

ContextType = dict


@strawberry.type
class CustomerQuery:
    @strawberry.field(permission_classes=[IsAuthenticated])
    def customers(self, info: Info[ContextType, None]) -> List[CustomerType]:  # noqa: PLR6301
        """Fetches all customers with their associated addresses."""
        db: Session = info.context['db']

        stmt = select(CustomerModel).order_by(CustomerModel.customerCode)
        result = db.execute(stmt)
        customers_db = result.scalars().unique().all()

        if not customers_db:
            return []

        return customers_db

    @strawberry.field(permission_classes=[IsAuthenticated])
    def customer(self, info: Info[ContextType, None], code: str) -> Optional[CustomerType]:  # noqa: PLR6301
        """Fetches a single customer by its code, including addresses."""
        db: Session = info.context['db']

        stmt = select(CustomerModel).where(CustomerModel.customerCode == code)

        result = db.execute(stmt)
        customer_db = result.scalars().unique().one_or_none()

        if not customer_db:
            return None

        return customer_db
