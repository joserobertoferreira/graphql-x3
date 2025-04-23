from typing import List, Optional

import strawberry

from app.graphql.types.address import Address as AddressType


@strawberry.type
class Site:
    code: str
    name: Optional[str]
    country: Optional[str]
    sales: int
    purchase: int
    accounting: int
    legalCompany: Optional[str]
    legislation: Optional[str]
    defaultAddress: Optional[str]

    siteAddresses: List[AddressType] = strawberry.field(
        description='List of addresses associated with this site (entityType=3)'
    )
