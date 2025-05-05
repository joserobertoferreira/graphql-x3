from typing import List, Optional

import strawberry
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from strawberry.types import Info

from app.graphql.types.site import Site as SiteType
from app.middleware.auth.permissions import IsAuthenticated
from app.models.corporation import Sites as SitesModel

ContextType = dict


@strawberry.type
class SiteQuery:
    @strawberry.field(permission_classes=[IsAuthenticated])
    def sites(self, info: Info[ContextType, None]) -> List[SiteType]:  # noqa: PLR6301
        """Fetches all sites with their associated addresses."""
        db: Session = info.context['db']

        stmt = select(SitesModel)
        result = db.execute(stmt)
        sites_db = result.scalars().unique().all()

        if not sites_db:
            return []

        return sites_db

    @strawberry.field(permission_classes=[IsAuthenticated])
    def site(self, info: Info[ContextType, None], code: str) -> Optional[SiteType]:  # noqa: PLR6301
        """Fetches a single site by its code, including addresses."""
        db: Session = info.context['db']

        stmt = select(SitesModel).where(SitesModel.code == code)

        result = db.execute(stmt)
        site_db = result.scalars().unique().one_or_none()

        if not site_db:
            return None

        return site_db
