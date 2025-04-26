from typing import TYPE_CHECKING, Annotated, List, Optional

import strawberry

from app.graphql.types.address import Address as AddressType

if TYPE_CHECKING:
    from app.graphql.types.site import Site


@strawberry.type
class Company:
    company: str
    companyName: Optional[str]
    isLegalCompany: Optional[int]
    legislation: Optional[str]
    country: Optional[str]
    defaultAddress: Optional[str]
    vatNumber: Optional[str]

    companyAddresses: List[AddressType] = strawberry.field(
        description='List of addresses associated with this company (entityType=2)'
    )

    companySites: List[Annotated['Site', strawberry.lazy('app.graphql.types.site')]] = strawberry.field(
        description='List of sites associated with this company',
    )

    # companySites: List['SiteType'] = strawberry.field(
    #     resolver=lambda root, info: list_sites(root, info),  # noqa: PLW0108
    #     description='List of sites associated with this company',
    # )
