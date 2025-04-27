from typing import List

from sqlalchemy.future import select
from sqlalchemy.orm import Session
from strawberry.types import Info

from app.database.utils import generate_select_query
from app.graphql.types.site import Site as SiteType
from app.models.corporation import Company, Sites


def list_sites(company: Company, info: Info) -> List[SiteType]:
    """Fetches all sites associated with a company."""

    db: Session = info.context['db']

    query = generate_select_query(Sites, SiteType, is_core=True)

    db_sites = []

    if query:
        stmt = select(query).where(Sites.company_code == company.company).order_by(Sites.site_code)
        result = db.execute(stmt)
        db_sites = result.scalars().all()

    return db_sites
