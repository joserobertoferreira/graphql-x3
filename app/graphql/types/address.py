from typing import List, Optional

import strawberry


@strawberry.type
class Address:
    entityType: int
    entityNumber: str
    code: str
    isDefault: int
    addressLine0: Optional[str]
    addressLine1: Optional[str]
    addressLine2: Optional[str]
    zipCode: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    countryName: Optional[str]
    phoneNumbers: List[Optional[str]]
    emails: List[Optional[str]]
    website: Optional[str]
