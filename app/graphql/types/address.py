from typing import Optional

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
    addressPhoneNumber0: Optional[str]
    addressPhoneNumber1: Optional[str]
    addressPhoneNumber2: Optional[str]
    addressPhoneNumber3: Optional[str]
    addressPhoneNumber4: Optional[str]
    addressEmail0: Optional[str]
    addressEmail1: Optional[str]
    addressEmail2: Optional[str]
    addressEmail3: Optional[str]
    addressEmail4: Optional[str]
    website: Optional[str]
