from typing import List, Optional

import strawberry
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from strawberry.types import Info

from app.graphql.types.company import Company as CompanyType
from app.models.corporation import Company as CompanyModel

ContextType = dict


@strawberry.type
class CompanyQuery:
    @strawberry.field
    def companies(self, info: Info[ContextType, None]) -> List[CompanyType]:  # noqa: PLR6301
        """Fetches all companies with their associated addresses."""
        db: Session = info.context['db']

        stmt = select(CompanyModel).order_by(CompanyModel.company)
        result = db.execute(stmt)
        companies_db = result.scalars().unique().all()

        if not companies_db:
            return []

        return companies_db

    @strawberry.field
    def company(self, info: Info[ContextType, None], company: str) -> Optional[CompanyType]:  # noqa: PLR6301
        """Fetches a single company by its company, including addresses."""
        db: Session = info.context['db']

        stmt = select(CompanyModel).where(CompanyModel.company == company)

        result = db.execute(stmt)
        company_db = result.scalars().unique().one_or_none()

        if not company_db:
            return None

        return company_db
