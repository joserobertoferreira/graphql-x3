from typing import TYPE_CHECKING, List

from sqlalchemy import Index, PrimaryKeyConstraint, SmallInteger, Unicode, text
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import (
    AuditMixin,
    DimensionMixin,
    DimensionTypesMixin,
    PrimaryKeyMixin,
)

if TYPE_CHECKING:
    from app.models.address import Address


class Sites(Base, AuditMixin, PrimaryKeyMixin, DimensionTypesMixin, DimensionMixin):
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
    unavailableDay0: Mapped[int] = mapped_column('UVYDAY_0', TINYINT, server_default=text('((0))'))
    unavailableDay1: Mapped[int] = mapped_column('UVYDAY_1', TINYINT, server_default=text('((0))'))
    unavailableDay2: Mapped[int] = mapped_column('UVYDAY_2', TINYINT, server_default=text('((0))'))
    unavailableDay3: Mapped[int] = mapped_column('UVYDAY_3', TINYINT, server_default=text('((0))'))
    unavailableDay4: Mapped[int] = mapped_column('UVYDAY_4', TINYINT, server_default=text('((0))'))
    unavailableDay5: Mapped[int] = mapped_column('UVYDAY_5', TINYINT, server_default=text('((0))'))
    unavailableDay6: Mapped[int] = mapped_column('UVYDAY_6', TINYINT, server_default=text('((0))'))
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
        overlaps='customerAddresses',
        lazy='selectin',
        cascade='save-update, merge, refresh-expire, expunge',
    )
