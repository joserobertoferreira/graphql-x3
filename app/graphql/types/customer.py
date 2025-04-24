from typing import List, Optional

import strawberry

from app.graphql.types.address import Address as AddressType


@strawberry.type
class Customer:
    customerCode: Optional[str]
    companyName: Optional[str]
    isActive: Optional[int]
    currency: Optional[str]
    paymentTerm: Optional[str]

    customerAddresses: List[AddressType] = strawberry.field(
        description='List of addresses associated with this site (entityType=1)'
    )
