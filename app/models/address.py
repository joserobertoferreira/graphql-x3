from typing import Optional

from sqlalchemy import Index, Integer, PrimaryKeyConstraint, Unicode, and_, text
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import Mapped, foreign, mapped_column, relationship

# import app.models.customer
# import app.models.sites
from app.database.base import Base
from app.database.mixins import AuditMixin, PrimaryKeyMixin

# if TYPE_CHECKING:
from app.models.customer import Customer
from app.models.sites import Sites

# Constants
ENTITY_TYPE_SITE = 3
ENTITY_TYPE_CUSTOMER = 1


class Address(Base, AuditMixin, PrimaryKeyMixin):
    """
    Model for the BPADDRESS table in the database.
    This table stores address information for business partners.
    """

    __tablename__ = 'BPADDRESS'
    __table_args__ = (
        PrimaryKeyConstraint('ROWID', name='BPADDRESS_ROWID'),
        Index('BPADDRESS_BPA0', 'BPATYP_0', 'BPANUM_0', 'BPAADD_0', unique=True),
        Index('BPADDRESS_SPE_BPA0', 'BPANUM_0', 'BPAADD_0'),
    )

    entityType: Mapped[int] = mapped_column('BPATYP_0', TINYINT, server_default=text('((1))'))
    entityNumber: Mapped[str] = mapped_column('BPANUM_0', Unicode(15, 'Latin1_General_BIN2'))
    code: Mapped[str] = mapped_column('BPAADD_0', Unicode(5, 'Latin1_General_BIN2'))
    description: Mapped[str] = mapped_column('BPADES_0', Unicode(30, 'Latin1_General_BIN2'), server_default=text("''"))
    defaultBankId: Mapped[str] = mapped_column(
        'BPABID_0', Unicode(30, 'Latin1_General_BIN2'), server_default=text("''")
    )
    isDefault: Mapped[int] = mapped_column('BPAADDFLG_0', TINYINT, server_default=text('((1))'))
    addressLine0: Mapped[str] = mapped_column(
        'BPAADDLIG_0', Unicode(50, 'Latin1_General_BIN2'), server_default=text("''")
    )
    addressLine1: Mapped[str] = mapped_column(
        'BPAADDLIG_1', Unicode(50, 'Latin1_General_BIN2'), server_default=text("''")
    )
    addressLine2: Mapped[str] = mapped_column(
        'BPAADDLIG_2', Unicode(50, 'Latin1_General_BIN2'), server_default=text("''")
    )
    zipCode: Mapped[str] = mapped_column('POSCOD_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''"))
    city: Mapped[str] = mapped_column('CTY_0', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''"))
    state: Mapped[str] = mapped_column('SAT_0', Unicode(35, 'Latin1_General_BIN2'), server_default=text("''"))
    country: Mapped[str] = mapped_column('CRY_0', Unicode(3, 'Latin1_General_BIN2'), server_default=text("''"))
    countryName: Mapped[str] = mapped_column('CRYNAM_0', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''"))
    addressPhoneNumber0: Mapped[str] = mapped_column(
        'TEL_0', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''")
    )
    addressPhoneNumber1: Mapped[str] = mapped_column(
        'TEL_1', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''")
    )
    addressPhoneNumber2: Mapped[str] = mapped_column(
        'TEL_2', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''")
    )
    addressPhoneNumber3: Mapped[str] = mapped_column(
        'TEL_3', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''")
    )
    addressPhoneNumber4: Mapped[str] = mapped_column(
        'TEL_4', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''")
    )
    fax: Mapped[str] = mapped_column('FAX_0', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''"))
    mobile: Mapped[str] = mapped_column('MOB_0', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''"))
    addressEmail0: Mapped[str] = mapped_column('WEB_0', Unicode(80, 'Latin1_General_BIN2'), server_default=text("''"))
    addressEmail1: Mapped[str] = mapped_column('WEB_1', Unicode(80, 'Latin1_General_BIN2'), server_default=text("''"))
    addressEmail2: Mapped[str] = mapped_column('WEB_2', Unicode(80, 'Latin1_General_BIN2'), server_default=text("''"))
    addressEmail3: Mapped[str] = mapped_column('WEB_3', Unicode(80, 'Latin1_General_BIN2'), server_default=text("''"))
    addressEmail4: Mapped[str] = mapped_column('WEB_4', Unicode(80, 'Latin1_General_BIN2'), server_default=text("''"))
    website: Mapped[str] = mapped_column('FCYWEB_0', Unicode(250, 'Latin1_General_BIN2'), server_default=text("''"))
    externalIdentifier: Mapped[str] = mapped_column(
        'EXTNUM_0', Unicode(30, 'Latin1_General_BIN2'), server_default=text("''")
    )
    exportNumber: Mapped[int] = mapped_column('EXPNUM_0', Integer, server_default=text('((0))'))
    codeINE: Mapped[str] = mapped_column('CODSEE_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    isValid: Mapped[int] = mapped_column('ADRVAL_0', TINYINT, server_default=text('((1))'))
    gln: Mapped[str] = mapped_column('GLNCOD_0', Unicode(13, 'Latin1_General_BIN2'), server_default=text("''"))
    crn: Mapped[str] = mapped_column('CRN_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))

    # site: Mapped[Optional['Sites']] = relationship(
    #     'Sites',
    #     primaryjoin=lambda: and_(Address.entityNumber == foreign(Sites.code), Address.entityType == ENTITY_TYPE_SITE),
    #     foreign_keys=[entityNumber],
    #     viewonly=True,
    #     back_populates='siteAddresses',
    #     lazy='joined',
    # )

    site: Mapped[Optional['Sites']] = relationship(
        'Sites',
        primaryjoin='and_(Address.entityNumber == foreign(Sites.code), Address.entityType == 3)',
        overlaps='siteAddresses',
        back_populates='siteAddresses',
        lazy='joined',
    )

    customer: Mapped[Optional['Customer']] = relationship(
        'Customer',
        primaryjoin=lambda: and_(
            Address.entityNumber == foreign(Customer.customerCode),
            Address.entityType == ENTITY_TYPE_CUSTOMER,
        ),
        foreign_keys=[entityNumber],
        viewonly=True,
        back_populates='customerAddresses',
        lazy='joined',
    )
