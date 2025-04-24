import datetime
import decimal
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import (
    DateTime,
    Index,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    SmallInteger,
    Unicode,
    text,
)
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.settings import DEFAULT_LEGACY_DATETIME
from app.database.base import Base
from app.database.generics_mixins import ArrayColumnMixin
from app.database.mixins import AuditMixin, CreateUpdateDateMixin, PrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.address import Address


class Customer(Base, AuditMixin, PrimaryKeyMixin, CreateUpdateDateMixin, ArrayColumnMixin):
    __tablename__ = 'BPCUSTOMER'
    __table_args__ = (
        PrimaryKeyConstraint('ROWID', name='BPCUSTOMER_ROWID'),
        Index('BPCUSTOMER_BPC0', 'BPCNUM_0', unique=True),
        Index('BPCUSTOMER_BPC1', 'BPCNAM_0'),
        Index('BPCUSTOMER_ZBPC0', 'ZCRYNAM_0', 'BPCNAM_0', 'BPCNUM_0', unique=True),
    )

    customerCode: Mapped[str] = mapped_column('BPCNUM_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''"))
    companyName: Mapped[str] = mapped_column('BPCNAM_0', Unicode(35, 'Latin1_General_BIN2'), server_default=text("''"))
    shortName: Mapped[str] = mapped_column('BPCSHO_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''"))
    category: Mapped[str] = mapped_column('BCGCOD_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    reminderGroup: Mapped[str] = mapped_column('GRP_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    customerType: Mapped[int] = mapped_column('BPCTYP_0', TINYINT, server_default=text('((1))'))
    billToCustomer: Mapped[str] = mapped_column(
        'BPCINV_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''")
    )
    billToCustomerAddress: Mapped[str] = mapped_column(
        'BPAINV_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    payByCustomer: Mapped[str] = mapped_column(
        'BPCPYR_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''")
    )
    payByCustomerAddress: Mapped[str] = mapped_column(
        'BPAPYR_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    groupCustomer: Mapped[str] = mapped_column(
        'BPCGRU_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''")
    )
    riskCustomer: Mapped[str] = mapped_column('BPCRSK_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''"))
    defaultAddress: Mapped[str] = mapped_column(
        'BPAADD_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    defaultShipToAddress: Mapped[str] = mapped_column(
        'BPDADD_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    defaultContact: Mapped[str] = mapped_column(
        'CNTNAM_0', Unicode(35, 'Latin1_General_BIN2'), server_default=text("''")
    )
    isActive: Mapped[int] = mapped_column('BPCSTA_0', TINYINT, server_default=text('((2))'))
    isProspect: Mapped[int] = mapped_column('PPTFLG_0', TINYINT, server_default=text('((1))'))
    ourSupplierCode: Mapped[str] = mapped_column(
        'BPCBPSNUM_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''")
    )
    factor: Mapped[str] = mapped_column('FCTNUM_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''"))
    currency: Mapped[str] = mapped_column('CUR_0', Unicode(3, 'Latin1_General_BIN2'), server_default=text("''"))
    rateType: Mapped[int] = mapped_column('CHGTYP_0', TINYINT, server_default=text('((1))'))
    commissionCategory: Mapped[int] = mapped_column('COMCAT_0', TINYINT, server_default=text('((1))'))
    salesRep0: Mapped[str] = mapped_column('REP_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''"))
    salesRep1: Mapped[str] = mapped_column('REP_1', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''"))
    taxRule: Mapped[str] = mapped_column('VACBPR_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    exemptionTaxNumber: Mapped[str] = mapped_column(
        'VATEXN_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''")
    )
    paymentTerm: Mapped[str] = mapped_column('PTE_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''"))
    freightInvoicing: Mapped[int] = mapped_column('FREINV_0', TINYINT, server_default=text('((1))'))
    earlyDiscount: Mapped[str] = mapped_column('DEP_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    priceType: Mapped[int] = mapped_column('PRITYP_0', TINYINT, server_default=text('((1))'))
    notes: Mapped[str] = mapped_column('BPCREM_0', Unicode(250, 'Latin1_General_BIN2'), server_default=text("''"))
    creditControl: Mapped[int] = mapped_column('OSTCTL_0', TINYINT, server_default=text('((2))'))
    authorizedCredit: Mapped[decimal.Decimal] = mapped_column('OSTAUZ_0', Numeric(27, 13), server_default=text('((0))'))
    minimumOrderAmount: Mapped[decimal.Decimal] = mapped_column(
        'ORDMINAMT_0', Numeric(27, 13), server_default=text('((0))')
    )
    creditInsurance: Mapped[decimal.Decimal] = mapped_column('CDTISR_0', Numeric(27, 13), server_default=text('((0))'))
    insuranceDate: Mapped[datetime.datetime] = mapped_column(
        'CDTISRDAT_0', DateTime, server_default=text(f"'{DEFAULT_LEGACY_DATETIME}'")
    )
    insuranceCompany: Mapped[str] = mapped_column(
        'BPCCDTISR_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''")
    )
    reminderType: Mapped[int] = mapped_column('FUPTYP_0', TINYINT, server_default=text('((1))'))
    minimumReminderAmount: Mapped[decimal.Decimal] = mapped_column(
        'FUPMINAMT_0', Numeric(27, 13), server_default=text('((0))')
    )
    noteType: Mapped[int] = mapped_column('SOIPER_0', TINYINT, server_default=text('((1))'))
    paymentBank: Mapped[str] = mapped_column('PAYBAN_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    accountingCode: Mapped[str] = mapped_column(
        'ACCCOD_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''")
    )
    canBeMatched: Mapped[int] = mapped_column('MTCFLG_0', TINYINT, server_default=text('((1))'))
    orderText: Mapped[str] = mapped_column('ORDTEX_0', Unicode(17, 'Latin1_General_BIN2'), server_default=text("''"))
    invoiceText: Mapped[str] = mapped_column('INVTEX_0', Unicode(17, 'Latin1_General_BIN2'), server_default=text("''"))
    loanAuthorized: Mapped[int] = mapped_column('LNDAUZ_0', TINYINT, server_default=text('((1))'))
    printAcknowledgment: Mapped[int] = mapped_column('OCNFLG_0', TINYINT, server_default=text('((1))'))
    invoicePeriod: Mapped[int] = mapped_column('INVPER_0', TINYINT, server_default=text('((1))'))
    dueDateOrigin: Mapped[int] = mapped_column('DUDCLC_0', TINYINT, server_default=text('((1))'))
    isOrderClosingAllowed: Mapped[int] = mapped_column('ORDCLE_0', TINYINT, server_default=text('((1))'))
    mustContainOneOrderPerDelivery: Mapped[int] = mapped_column('ODL_0', TINYINT, server_default=text('((2))'))
    partialDelivery: Mapped[int] = mapped_column('DME_0', TINYINT, server_default=text('((2))'))
    invoiceMode: Mapped[int] = mapped_column('IME_0', TINYINT, server_default=text('((1))'))
    businessSector: Mapped[str] = mapped_column('BUS_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))
    prospectOrigin: Mapped[str] = mapped_column(
        'ORIPPT_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''")
    )
    tokenCredit: Mapped[int] = mapped_column('PITCDT_0', Integer, server_default=text('((0))'))
    manualAdditionalToken: Mapped[int] = mapped_column('PITCPT_0', Integer, server_default=text('((0))'))
    totalTokenCredit: Mapped[int] = mapped_column('TOTPIT_0', Integer, server_default=text('((0))'))
    serviceContract: Mapped[str] = mapped_column(
        'COTCHX_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''")
    )
    necessaryTokens: Mapped[int] = mapped_column('COTPITRQD_0', Integer, server_default=text('((0))'))
    firstContactDate: Mapped[datetime.datetime] = mapped_column(
        'CNTFIRDAT_0', DateTime, server_default=text(f"'{DEFAULT_LEGACY_DATETIME}'")
    )
    lastContactDate: Mapped[datetime.datetime] = mapped_column(
        'CNTLASDAT_0', DateTime, server_default=text(f"'{DEFAULT_LEGACY_DATETIME}'")
    )
    nextContactDate: Mapped[datetime.datetime] = mapped_column(
        'CNTNEXDAT_0', DateTime, server_default=text(f"'{DEFAULT_LEGACY_DATETIME}'")
    )
    lastContactType: Mapped[int] = mapped_column('CNTLASTYP_0', TINYINT, server_default=text('((1))'))
    nextContactType: Mapped[int] = mapped_column('CNTNEXTYP_0', TINYINT, server_default=text('((1))'))
    firstOrderDate: Mapped[datetime.datetime] = mapped_column(
        'ORDFIRDAT_0', DateTime, server_default=text(f"'{DEFAULT_LEGACY_DATETIME}'")
    )
    lastQuoteDate: Mapped[datetime.datetime] = mapped_column(
        'QUOLASDAT_0', DateTime, server_default=text(f"'{DEFAULT_LEGACY_DATETIME}'")
    )
    classABC: Mapped[int] = mapped_column('ABCCLS_0', TINYINT, server_default=text('((1))'))
    vatCollectionAgent: Mapped[int] = mapped_column('AGTPCP_0', SmallInteger, server_default=text('((0))'))
    regionalTaxesAgent: Mapped[int] = mapped_column('AGTSATTAX_0', SmallInteger, server_default=text('((0))'))
    provinceCode: Mapped[str] = mapped_column('SATTAX_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    collectionAgent: Mapped[int] = mapped_column('FLGSATTAX_0', SmallInteger, server_default=text('((0))'))
    printTemplate: Mapped[str] = mapped_column('TPMCOD_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    accountStructure: Mapped[str] = mapped_column(
        'DIA_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''")
    )
    customerSince: Mapped[datetime.datetime] = mapped_column(
        'BPCSNCDAT_0', DateTime, server_default=text(f"'{DEFAULT_LEGACY_DATETIME}'")
    )
    exportNumber: Mapped[int] = mapped_column('EXPNUM_0', Integer, server_default=text('((0))'))
    unavailablePeriod: Mapped[str] = mapped_column(
        'UVYCOD2_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    isSubjectToTax: Mapped[int] = mapped_column('BELVATSUB_0', SmallInteger, server_default=text('((0))'))
    invoicingTerm: Mapped[str] = mapped_column(
        'INVCND_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''")
    )
    isElectronicInvoice: Mapped[int] = mapped_column('ELECTINV_0', TINYINT, server_default=text('((1))'))
    contact: Mapped[str] = mapped_column('CNTEFAT_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''"))
    startDataElectronicInvoice: Mapped[datetime.datetime] = mapped_column(
        'STRDATEFAT_0', DateTime, server_default=text(f"'{DEFAULT_LEGACY_DATETIME}'")
    )
    isElectronicInvoiceAllowed: Mapped[int] = mapped_column('AEIFLG_0', SmallInteger, server_default=text('((0))'))
    isEditor: Mapped[int] = mapped_column('ZEDITOR_0', TINYINT, server_default=text('((1))'))
    isAgent: Mapped[int] = mapped_column('ZAGENTE_0', TINYINT, server_default=text('((1))'))
    interface: Mapped[int] = mapped_column('ZINTVSP_0', TINYINT, server_default=text('((1))'))
    settlementDiscount: Mapped[decimal.Decimal] = mapped_column(
        'ZDISCRGVAL_0', Numeric(10, 3), server_default=text('((0))')
    )
    exports: Mapped[int] = mapped_column('ZEXPFLG_0', TINYINT, server_default=text('((1))'))
    countryExport: Mapped[str] = mapped_column(
        'ZCRYNAM_0', Unicode(40, 'Latin1_General_BIN2'), server_default=text("''")
    )

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='TSCCOD',
        property_name='statistical',
        count=5,
        column_type=Unicode(20, 'Latin1_General_BIN2'),
        python_type=str,
        server_default=text("''"),
    )

    statisticalGroup: Mapped[List[Optional[str]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='DIE',
        property_name='dimensionType',
        count=20,
        column_type=Unicode(10, 'Latin1_General_BIN2'),
        python_type=str,
        server_default=text("''"),
    )

    dimensionsType: Mapped[List[Optional[str]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='CCE',
        property_name='dimension',
        count=20,
        column_type=Unicode(15, 'Latin1_General_BIN2'),
        python_type=str,
        server_default=text("''"),
    )

    dimensions: Mapped[List[Optional[str]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='INVDTAAMT',
        property_name='invdtaamt',
        count=30,
        column_type=Numeric(20, 5),
        python_type=decimal.Decimal,
        server_default=text('((0))'),
    )

    percentageOrAmount: Mapped[List[Optional[decimal.Decimal]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='INVDTA',
        property_name='invdta',
        count=30,
        column_type=SmallInteger,
        python_type=int,
        server_default=text('((0))'),
    )

    invoicingElement: Mapped[List[Optional[int]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='DAYMON',
        property_name='paymentDay',
        count=6,
        column_type=SmallInteger,
        python_type=int,
        server_default=text('((0))'),
    )

    paymentDay: Mapped[List[Optional[int]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='CSHVATRGM',
        property_name='cashIsActive',
        count=9,
        column_type=TINYINT,
        python_type=int,
        server_default=text('((0))'),
    )

    cashIsActive: Mapped[List[Optional[int]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='VATSTRDAT',
        property_name='vatStartDate',
        count=9,
        column_type=DateTime,
        python_type=datetime.datetime,
        server_default=text(f"'{DEFAULT_LEGACY_DATETIME}'"),
    )

    vatStartDate: Mapped[List[Optional[datetime.datetime]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='VATENDDAT',
        property_name='vatEndDate',
        count=9,
        column_type=DateTime,
        python_type=datetime.datetime,
        server_default=text(f"'{DEFAULT_LEGACY_DATETIME}'"),
    )

    vatEndDate: Mapped[List[Optional[datetime.datetime]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    customerAddresses: Mapped[List['Address']] = relationship(
        'Address',
        primaryjoin='and_(Address.entityNumber == Customer.customerCode, Address.entityType == 1)',
        foreign_keys='Address.entityNumber',
        overlaps='siteAddresses',
        lazy='selectin',
        cascade='save-update, merge, refresh-expire, expunge',
    )
