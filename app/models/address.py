from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Index, Integer, PrimaryKeyConstraint, Unicode, text
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.database.generics_mixins import ArrayColumnMixin
from app.database.mixins import AuditMixin, PrimaryKeyMixin

if TYPE_CHECKING:
    pass


class Address(Base, AuditMixin, PrimaryKeyMixin, ArrayColumnMixin):
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

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='TEL',
        property_name='phoneNumber',
        count=5,
        column_type=Unicode(40, 'Latin1_General_BIN2'),
        python_type=str,
        server_default=text("''"),
    )

    phoneNumbers: Mapped[List[Optional[str]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    fax: Mapped[str] = mapped_column('FAX_0', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''"))
    mobile: Mapped[str] = mapped_column('MOB_0', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''"))

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='WEB',
        property_name='email',
        count=5,
        column_type=Unicode(80, 'Latin1_General_BIN2'),
        python_type=str,
        server_default=text("''"),
    )

    emails: Mapped[List[Optional[str]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    website: Mapped[str] = mapped_column('FCYWEB_0', Unicode(250, 'Latin1_General_BIN2'), server_default=text("''"))
    externalIdentifier: Mapped[str] = mapped_column(
        'EXTNUM_0', Unicode(30, 'Latin1_General_BIN2'), server_default=text("''")
    )
    exportNumber: Mapped[int] = mapped_column('EXPNUM_0', Integer, server_default=text('((0))'))
    codeINE: Mapped[str] = mapped_column('CODSEE_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    isValid: Mapped[int] = mapped_column('ADRVAL_0', TINYINT, server_default=text('((1))'))
    gln: Mapped[str] = mapped_column('GLNCOD_0', Unicode(13, 'Latin1_General_BIN2'), server_default=text("''"))
    crn: Mapped[str] = mapped_column('CRN_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))
