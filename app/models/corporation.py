import datetime
import decimal
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Date, Index, Numeric, PrimaryKeyConstraint, SmallInteger, Unicode, text
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.settings import DEFAULT_LEGACY_DATE
from app.database.base import Base
from app.database.generics_mixins import ArrayColumnMixin
from app.database.mixins import AuditMixin, CreateUpdateDateMixin, PrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.address import Address


class Sites(Base, AuditMixin, PrimaryKeyMixin, CreateUpdateDateMixin, ArrayColumnMixin):
    __tablename__ = 'FACILITY'
    __table_args__ = (
        PrimaryKeyConstraint('ROWID', name='FACILITY_ROWID'),
        Index('FACILITY_FCY0', 'FCY_0', unique=True),
        Index('FACILITY_FCY1', 'LEGCPY_0', 'FCY_0', unique=True),
    )

    code: Mapped[str] = mapped_column('FCY_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    name: Mapped[str] = mapped_column('FCYNAM_0', Unicode(35, 'Latin1_General_BIN2'), server_default=text("''"))
    shortName: Mapped[str] = mapped_column('FCYSHO_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''"))
    country: Mapped[str] = mapped_column('CRY_0', Unicode(3, 'Latin1_General_BIN2'), server_default=text("''"))
    crn: Mapped[str] = mapped_column('CRN_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))
    naf: Mapped[str] = mapped_column('NAF_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''"))
    carrier: Mapped[str] = mapped_column('BPTNUM_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''"))
    manufacturing: Mapped[int] = mapped_column('MFGFLG_0', TINYINT, server_default=text('((1))'))
    sales: Mapped[int] = mapped_column('SALFLG_0', TINYINT, server_default=text('((1))'))
    purchase: Mapped[int] = mapped_column('PURFLG_0', TINYINT, server_default=text('((1))'))
    isStockSite: Mapped[int] = mapped_column('WRHFLG_0', TINYINT, server_default=text('((1))'))
    accounting: Mapped[int] = mapped_column('FINFLG_0', TINYINT, server_default=text('((1))'))
    financialSite: Mapped[str] = mapped_column(
        'FINRSPFCY_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    das2: Mapped[int] = mapped_column('DADFLG_0', SmallInteger, server_default=text('((0))'))
    paymentBank: Mapped[str] = mapped_column('PAYBAN_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    legalCompany: Mapped[str] = mapped_column('LEGCPY_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    legislation: Mapped[str] = mapped_column('LEG_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))
    defaultAddress: Mapped[str] = mapped_column(
        'BPAADD_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    bankAccountNumber: Mapped[str] = mapped_column(
        'BIDNUM_0', Unicode(30, 'Latin1_General_BIN2'), server_default=text("''")
    )
    contact: Mapped[str] = mapped_column('CNTNAM_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''"))
    das2Site: Mapped[str] = mapped_column('DADFCY_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    accountingCode: Mapped[str] = mapped_column(
        'ACCCOD_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''")
    )
    geographicCode: Mapped[str] = mapped_column(
        'GEOCOD_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    eoriNumber: Mapped[str] = mapped_column('EORINUM_0', Unicode(35, 'Latin1_General_BIN2'), server_default=text("''"))
    selfCertificationOrigin: Mapped[int] = mapped_column('ORICERFLG_0', TINYINT, server_default=text('((1))'))
    rexNumber: Mapped[str] = mapped_column('REXNUM_0', Unicode(30, 'Latin1_General_BIN2'), server_default=text("''"))
    cityInteriorFlag: Mapped[str] = mapped_column(
        'INSCTYFLG_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )

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
        db_column_prefix='UVYDAY',
        property_name='unavailableDay',
        count=7,
        column_type=TINYINT,
        python_type=int,
        server_default=text('((0))'),
    )

    unavailableDays: Mapped[List[Optional[int]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    unavailable: Mapped[str] = mapped_column('UVYCOD_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    countFlag: Mapped[int] = mapped_column('IVYFLG_0', TINYINT, server_default=text('((1))'))
    stockCountSite: Mapped[str] = mapped_column(
        'IVYFCY_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    warehouse: Mapped[int] = mapped_column('WRHGES_0', TINYINT, server_default=text('((1))'))
    receiptWrh: Mapped[str] = mapped_column('RCPWRH_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    workOrderWrh: Mapped[str] = mapped_column('MFPWRH_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    IntReceipt: Mapped[str] = mapped_column('TRAWRH_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    deliveryReturnWrh: Mapped[str] = mapped_column(
        'RTNWRH_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    reintegrationWrh: Mapped[str] = mapped_column(
        'MFRWRH_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    shipmentWrh: Mapped[str] = mapped_column('SHIWRH_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    consWrh: Mapped[str] = mapped_column('MFGWRH_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    issueWhr: Mapped[str] = mapped_column('TRFWRH_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    subContractWrh: Mapped[str] = mapped_column(
        'SCOWRH_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    subConsWrh: Mapped[str] = mapped_column('SCCWRH_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    igicOperations: Mapped[int] = mapped_column('SPAOPEIGIC_0', SmallInteger, server_default=text('((0))'))
    starHour: Mapped[str] = mapped_column('STRHOU_0', Unicode(6, 'Latin1_General_BIN2'), server_default=text("''"))
    endHour: Mapped[str] = mapped_column('ENDHOU_0', Unicode(6, 'Latin1_General_BIN2'), server_default=text("''"))
    hrmPayroll: Mapped[int] = mapped_column('PAYFLG_0', SmallInteger, server_default=text('((0))'))
    hrmDadsFlag: Mapped[int] = mapped_column('HRMDADFLG_0', SmallInteger, server_default=text('((0))'))
    hrmDadsSite: Mapped[str] = mapped_column(
        'HRMDADFCY_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    hrmHeadquartersAddress: Mapped[str] = mapped_column(
        'BPASGE_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    hrmDeclaringAddress: Mapped[str] = mapped_column(
        'BPADCL_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    hrmTdsContact: Mapped[str] = mapped_column('CNTDDS_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    hrmCramCode: Mapped[str] = mapped_column('CODCRA_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    hrmIndustrialTribunal: Mapped[int] = mapped_column('REGPRH_0', SmallInteger, server_default=text('((0))'))
    hrmProfile: Mapped[str] = mapped_column('PRF_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    hrmDepartment: Mapped[str] = mapped_column('SRV_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    hrmCollectiveAgreement: Mapped[str] = mapped_column(
        'CLLCVT_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    hrmRisk: Mapped[str] = mapped_column('RSKWRK_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    hrmBank: Mapped[str] = mapped_column('HRMPAYBAN_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    hrmTaxSalaries: Mapped[int] = mapped_column('HRMTAXWAG_0', SmallInteger, server_default=text('((0))'))
    hrmDerogation: Mapped[int] = mapped_column('SECPRH_0', SmallInteger, server_default=text('((0))'))
    hrmApprenticeship: Mapped[int] = mapped_column('FLGAPP_0', SmallInteger, server_default=text('((0))'))
    hrmTraining: Mapped[int] = mapped_column('FLGFOR_0', SmallInteger, server_default=text('((0))'))
    hrmHousing: Mapped[int] = mapped_column('FLGPEC_0', SmallInteger, server_default=text('((0))'))
    hrmSupervisor: Mapped[str] = mapped_column('CHEF_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    serviceID: Mapped[str] = mapped_column('SERVICEID_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))

    siteAddresses: Mapped[List['Address']] = relationship(
        'Address',
        primaryjoin='and_(Address.entityNumber == Sites.code, Address.entityType == 3)',
        foreign_keys='Address.entityNumber',
        overlaps='customerAddresses, companyAddresses',
        lazy='selectin',
        cascade='save-update, merge, refresh-expire, expunge',
    )

    company: Mapped['Company'] = relationship(
        'Company',
        primaryjoin='and_(Company.company == Sites.legalCompany)',
        foreign_keys='Company.company',
        lazy='selectin',
        cascade='save-update, merge, refresh-expire, expunge',
    )


class Company(Base, AuditMixin, PrimaryKeyMixin, CreateUpdateDateMixin, ArrayColumnMixin):
    __tablename__ = 'COMPANY'
    __table_args__ = (
        PrimaryKeyConstraint('ROWID', name='COMPANY_ROWID'),
        Index('COMPANY_CPY0', 'CPY_0', unique=True),
        Index('COMPANY_CPY1', 'LEG_0', 'CPY_0'),
    )

    company: Mapped[str] = mapped_column('CPY_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    companyName: Mapped[str] = mapped_column('CPYNAM_0', Unicode(35, 'Latin1_General_BIN2'), server_default=text("''"))
    shortName: Mapped[str] = mapped_column('CPYSHO_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''"))
    isLegalCompany: Mapped[int] = mapped_column('CPYLEGFLG_0', TINYINT, server_default=text('((2))'))
    legislation: Mapped[str] = mapped_column('LEG_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))
    accountModel: Mapped[str] = mapped_column('ACM_0', Unicode(3, 'Latin1_General_BIN2'), server_default=text("''"))
    mainSite: Mapped[str] = mapped_column('MAIFCY_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''"))
    country: Mapped[str] = mapped_column('CRY_0', Unicode(3, 'Latin1_General_BIN2'), server_default=text("''"))
    taxIDNumber: Mapped[str] = mapped_column('CRN_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))
    sicCode: Mapped[str] = mapped_column('NAF_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''"))
    idNumber: Mapped[str] = mapped_column('NID_0', Unicode(80, 'Latin1_General_BIN2'), server_default=text("''"))
    legalForm: Mapped[str] = mapped_column('CPYLOG_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''"))
    registeredCapital: Mapped[decimal.Decimal] = mapped_column('RGCAMT_0', Numeric(20, 5), server_default=text('((0))'))
    registeredCapitalCurrency: Mapped[str] = mapped_column(
        'RGCCUR_0', Unicode(3, 'Latin1_General_BIN2'), server_default=text("''")
    )
    defaultAddress: Mapped[str] = mapped_column(
        'BPAADD_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    contact: Mapped[str] = mapped_column('CNTNAM_0', Unicode(15, 'Latin1_General_BIN2'), server_default=text("''"))
    bankAccountNumber: Mapped[str] = mapped_column(
        'BIDNUM_0', Unicode(30, 'Latin1_General_BIN2'), server_default=text("''")
    )
    accountingCode: Mapped[str] = mapped_column(
        'ACCCOD_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''")
    )
    divisionCode: Mapped[str] = mapped_column('DIVCOD_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    vatNumber: Mapped[str] = mapped_column('EECNUM_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))
    x3Folder: Mapped[str] = mapped_column('FDRX3_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    firstFiscalYear: Mapped[datetime.date] = mapped_column(
        'STRPER_0', Date, server_default=text(f"'{DEFAULT_LEGACY_DATE}'")
    )
    accountingCurrency: Mapped[str] = mapped_column(
        'ACCCUR_0', Unicode(3, 'Latin1_General_BIN2'), server_default=text("''")
    )
    cysActivity: Mapped[str] = mapped_column('KACT_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))
    additionalNumber: Mapped[int] = mapped_column('NUMADD_0', SmallInteger, server_default=text('((0))'))
    selfCertificationOrigin: Mapped[int] = mapped_column('ORICERFLG_0', TINYINT, server_default=text('((1))'))
    eoriNumber: Mapped[str] = mapped_column('EORINUM_0', Unicode(35, 'Latin1_General_BIN2'), server_default=text("''"))

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
        db_column_prefix='OBYDIE',
        property_name='mandatoryDimensionType',
        count=20,
        column_type=TINYINT,
        python_type=int,
        server_default=text('((1))'),
    )

    mandatoryDimensionsType: Mapped[List[Optional[int]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='DACDIE',
        property_name='upstreamEnter',
        count=20,
        column_type=TINYINT,
        python_type=int,
        server_default=text('((1))'),
    )

    dimensionsAscending: Mapped[List[Optional[int]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    rexNumber: Mapped[str] = mapped_column('REXNUM_0', Unicode(30, 'Latin1_General_BIN2'), server_default=text("''"))
    federalState: Mapped[str] = mapped_column('STAFED_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    consolidation: Mapped[str] = mapped_column('GRUCOD_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    structureCode: Mapped[str] = mapped_column(
        'PLISTC_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''")
    )
    retained: Mapped[int] = mapped_column('RTZFLG_0', SmallInteger, server_default=text('((0))'))
    collectionAgent: Mapped[int] = mapped_column('AGTPCP_0', SmallInteger, server_default=text('((0))'))
    taxRule: Mapped[str] = mapped_column('VACCPY_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    directReport: Mapped[int] = mapped_column('DCLDIRBALPAY_0', TINYINT, server_default=text('((1))'))
    economicReason: Mapped[str] = mapped_column(
        'BDFECOCOD_0', Unicode(10, 'Latin1_General_BIN2'), server_default=text("''")
    )
    financialDeptAustria: Mapped[str] = mapped_column(
        'AUSFINSRV_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    defaultValue: Mapped[int] = mapped_column('GERDEFVAL_0', SmallInteger, server_default=text('((0))'))
    taxNumber: Mapped[str] = mapped_column('GEREECNUM_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    taxCenter: Mapped[str] = mapped_column('GERTAXCEN_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    taxIdentifier: Mapped[str] = mapped_column(
        'GERTAXIDT_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    elma5ID: Mapped[str] = mapped_column('GERCODELMA5_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    attendee: Mapped[str] = mapped_column('GERPTP_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    customerThreshold: Mapped[decimal.Decimal] = mapped_column(
        'SPABPCTSD_0', Numeric(28, 8), server_default=text('((0))')
    )
    supplierThreshold: Mapped[decimal.Decimal] = mapped_column(
        'SPABPSTSD_0', Numeric(28, 8), server_default=text('((0))')
    )
    yearlyThreshold: Mapped[decimal.Decimal] = mapped_column(
        'SPAYEATSD_0', Numeric(28, 8), server_default=text('((0))')
    )
    certifiedExpert: Mapped[str] = mapped_column(
        'PORCTFACN_0', Unicode(9, 'Latin1_General_BIN2'), server_default=text("''")
    )
    companyActivity: Mapped[str] = mapped_column(
        'PORCPYACT_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    periodicity: Mapped[int] = mapped_column('PORDCLPER_0', TINYINT)
    legalRepresentative: Mapped[str] = mapped_column(
        'PORLRC_0', Unicode(9, 'Latin1_General_BIN2'), server_default=text("''")
    )
    headOffice: Mapped[int] = mapped_column('PORHQR_0', TINYINT, server_default=text('((1))'))
    detailedActivity: Mapped[str] = mapped_column(
        'PORCPYACTDET_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    financialDepartment: Mapped[str] = mapped_column(
        'PORFINDPR_0', Unicode(9, 'Latin1_General_BIN2'), server_default=text("''")
    )
    sepaID: Mapped[str] = mapped_column('SCINUM_0', Unicode(35, 'Latin1_General_BIN2'), server_default=text("''"))
    activityType: Mapped[int] = mapped_column('PORCPYACTTYP_0', TINYINT, server_default=text('((1))'))
    simplifiedInvoice: Mapped[int] = mapped_column('PORSIMINVISS_0', TINYINT, server_default=text('((1))'))
    simplifiedInvoiceService: Mapped[decimal.Decimal] = mapped_column(
        'PORAMTSERINV_0', Numeric(14, 3), server_default=text('((0))')
    )
    simplifiedInvoiceItems: Mapped[decimal.Decimal] = mapped_column(
        'PORAMTITMINV_0', Numeric(14, 3), server_default=text('((0))')
    )
    invoicingCompany: Mapped[str] = mapped_column(
        'PORRESFISCDA_0', Unicode(5, 'Latin1_General_BIN2'), server_default=text("''")
    )
    activation: Mapped[int] = mapped_column('SSTTAXACT_0', SmallInteger, server_default=text('((0))'))
    sstCompany: Mapped[str] = mapped_column('SSTCPY_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    invoicingElement: Mapped[int] = mapped_column('SFINUM_0', SmallInteger, server_default=text('((0))'))
    longDescription: Mapped[str] = mapped_column(
        'ZDESLONG_0', Unicode(150, 'Latin1_General_BIN2'), server_default=text("''")
    )
    ZSQHTEX_0: Mapped[str] = mapped_column(Unicode(17, 'Latin1_General_BIN2'), server_default=text("''"))

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='COMMTYPE',
        property_name='commType',
        count=9,
        column_type=TINYINT,
        python_type=int,
        server_default=text('((1))'),
    )

    communicationType: Mapped[List[Optional[int]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='STRDAT',
        property_name='startDate',
        count=9,
        column_type=Date,
        python_type=datetime.date,
        server_default=text(f"'{DEFAULT_LEGACY_DATE}'"),
    )

    startDates: Mapped[List[Optional[datetime.date]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    _properties, _columns = ArrayColumnMixin.create_array_property(
        db_column_prefix='ENDDAT',
        property_name='endDate',
        count=9,
        column_type=Date,
        python_type=datetime.date,
        server_default=text(f"'{DEFAULT_LEGACY_DATE}'"),
    )

    endDates: Mapped[List[Optional[datetime.date]]] = _properties

    for _attr_name, _mapped_column in _columns.items():
        locals()[_attr_name] = _mapped_column

    del _attr_name, _mapped_column, _properties, _columns

    taxAgencyNumber: Mapped[str] = mapped_column(
        'TAXAGCNUM_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    taxAgencyName: Mapped[str] = mapped_column(
        'TAXAGCNAM_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    taxAgentNumber: Mapped[str] = mapped_column(
        'TAXAGNNUM_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    taxAgentName: Mapped[str] = mapped_column(
        'TAXAGNNAM_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    arabicName: Mapped[str] = mapped_column('ARACPYNAM_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    gosiReference: Mapped[str] = mapped_column(
        'GOSIREFNUM_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    sector1: Mapped[str] = mapped_column('SCT1_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))
    molEstablishmentID: Mapped[str] = mapped_column(
        'MOLID_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    sector2: Mapped[str] = mapped_column('SCT2_0', Unicode(20, 'Latin1_General_BIN2'), server_default=text("''"))
    customerTRId: Mapped[str] = mapped_column('TRECPY_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    customerCDId: Mapped[str] = mapped_column('TRECPY2_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    location: Mapped[int] = mapped_column('IMPCPY_0', SmallInteger, server_default=text('((0))'))
    wasteDBNumber: Mapped[str] = mapped_column('BDO_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    agreement: Mapped[str] = mapped_column('AGREEMENT_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    serviceId: Mapped[str] = mapped_column('SERVICEID_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''"))
    startPeriod: Mapped[datetime.date] = mapped_column(
        'INIPER_0', Date, server_default=text(f"'{DEFAULT_LEGACY_DATE}'")
    )
    finalPeriod: Mapped[datetime.date] = mapped_column(
        'FINPER_0', Date, server_default=text(f"'{DEFAULT_LEGACY_DATE}'")
    )
    solutionFunding: Mapped[str] = mapped_column(
        'SOLFIN_0', Unicode(1, 'Latin1_General_BIN2'), server_default=text("''")
    )
    financialAmount: Mapped[decimal.Decimal] = mapped_column('AMTFIN_0', Numeric(28, 8), server_default=text('((0))'))

    companyAddresses: Mapped[List['Address']] = relationship(
        'Address',
        primaryjoin='and_(Address.entityNumber == Company.company, Address.entityType == 2)',
        foreign_keys='Address.entityNumber',
        overlaps='customerAddresses, siteAddresses',
        lazy='selectin',
        cascade='save-update, merge, refresh-expire, expunge',
    )

    companySites: Mapped[List[Sites]] = relationship(
        'Sites',
        primaryjoin='and_(Company.company == Sites.legalCompany)',
        foreign_keys='Sites.legalCompany',
        lazy='selectin',
        cascade='save-update, merge, refresh-expire, expunge',
    )
