import datetime
import decimal

from sqlalchemy import (
    BINARY,
    DateTime,
    Identity,
    Index,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    SmallInteger,
    Unicode,
    text,
)
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.database.base import Base


class Base(DeclarativeBase):
    pass


class Partner(Base):
    __tablename__ = 'BPARTNER'
    __table_args__ = (
        PrimaryKeyConstraint('ROWID', name='BPARTNER_ROWID'),
        Index('BPARTNER_BPR0', 'BPRNUM_0', unique=True),
        Index('BPARTNER_BPR1', 'BPRSHO_0'),
        Index('BPARTNER_BPR2', 'BETFCY_0', 'FCY_0', 'BPRNUM_0', unique=True),
    )

    UPDTICK_0: Mapped[int] = mapped_column(Integer, server_default=text('((1))'))
    BPRNUM_0: Mapped[str] = mapped_column(Unicode(15, 'Latin1_General_BIN2'))
    ENAFLG_0: Mapped[int] = mapped_column(TINYINT)
    BRGCOD_0: Mapped[str] = mapped_column(Unicode(5, 'Latin1_General_BIN2'))
    BRGOBJ_0: Mapped[str] = mapped_column(Unicode(3, 'Latin1_General_BIN2'))
    BPRNAM_0: Mapped[str] = mapped_column(Unicode(35, 'Latin1_General_BIN2'))
    BPRNAM_1: Mapped[str] = mapped_column(Unicode(35, 'Latin1_General_BIN2'))
    BPRSHO_0: Mapped[str] = mapped_column(Unicode(10, 'Latin1_General_BIN2'))
    EECNUM_0: Mapped[str] = mapped_column(Unicode(20, 'Latin1_General_BIN2'))
    BETFCY_0: Mapped[int] = mapped_column(TINYINT)
    FCY_0: Mapped[str] = mapped_column(Unicode(5, 'Latin1_General_BIN2'))
    CRY_0: Mapped[str] = mapped_column(Unicode(3, 'Latin1_General_BIN2'))
    CRN_0: Mapped[str] = mapped_column(Unicode(20, 'Latin1_General_BIN2'))
    NAF_0: Mapped[str] = mapped_column(Unicode(1, 'Latin1_General_BIN2'))
    CUR_0: Mapped[str] = mapped_column(Unicode(3, 'Latin1_General_BIN2'))
    LAN_0: Mapped[str] = mapped_column(Unicode(3, 'Latin1_General_BIN2'))
    BPRLOG_0: Mapped[str] = mapped_column(Unicode(10, 'Latin1_General_BIN2'))
    VATNUM_0: Mapped[str] = mapped_column(Unicode(1, 'Latin1_General_BIN2'))
    FISCOD_0: Mapped[str] = mapped_column(Unicode(1, 'Latin1_General_BIN2'))
    GRUGPY_0: Mapped[str] = mapped_column(Unicode(5, 'Latin1_General_BIN2'))
    GRUCOD_0: Mapped[str] = mapped_column(Unicode(1, 'Latin1_General_BIN2'))
    BPCFLG_0: Mapped[int] = mapped_column(TINYINT)
    BPSFLG_0: Mapped[int] = mapped_column(TINYINT)
    CCNFLG_0: Mapped[int] = mapped_column(SmallInteger)
    BPTFLG_0: Mapped[int] = mapped_column(TINYINT)
    FCTFLG_0: Mapped[int] = mapped_column(TINYINT)
    REPFLG_0: Mapped[int] = mapped_column(TINYINT)
    BPRACC_0: Mapped[int] = mapped_column(TINYINT)
    PPTFLG_0: Mapped[int] = mapped_column(TINYINT)
    PRVFLG_0: Mapped[int] = mapped_column(TINYINT)
    DOOFLG_0: Mapped[int] = mapped_column(TINYINT)
    ACCCOD_0: Mapped[str] = mapped_column(Unicode(10, 'Latin1_General_BIN2'))
    PTHFLG_0: Mapped[int] = mapped_column(SmallInteger)
    BPRFLG_0: Mapped[int] = mapped_column(TINYINT)
    BPRFLG_1: Mapped[int] = mapped_column(TINYINT)
    BPRFLG_2: Mapped[int] = mapped_column(TINYINT)
    BPRFLG_3: Mapped[int] = mapped_column(TINYINT)
    BPAADD_0: Mapped[str] = mapped_column(Unicode(5, 'Latin1_General_BIN2'))
    CNTNAM_0: Mapped[str] = mapped_column(Unicode(35, 'Latin1_General_BIN2'))
    BIDNUM_0: Mapped[str] = mapped_column(Unicode(30, 'Latin1_General_BIN2'))
    BIDCRY_0: Mapped[str] = mapped_column(Unicode(3, 'Latin1_General_BIN2'))
    ACS_0: Mapped[str] = mapped_column(Unicode(10, 'Latin1_General_BIN2'))
    EXPNUM_0: Mapped[int] = mapped_column(Integer)
    BPRGTETYP_0: Mapped[str] = mapped_column(Unicode(5, 'Latin1_General_BIN2'))
    BPRFBDMAG_0: Mapped[int] = mapped_column(TINYINT)
    MODPAM_0: Mapped[str] = mapped_column(Unicode(20, 'Latin1_General_BIN2'))
    ACCNONREI_0: Mapped[str] = mapped_column(Unicode(5, 'Latin1_General_BIN2'))
    LEGETT_0: Mapped[int] = mapped_column(TINYINT)
    CFOEXD_0: Mapped[int] = mapped_column(TINYINT)
    CREUSR_0: Mapped[str] = mapped_column(Unicode(5, 'Latin1_General_BIN2'))
    CREDAT_0: Mapped[datetime.datetime] = mapped_column(DateTime)
    UPDUSR_0: Mapped[str] = mapped_column(Unicode(5, 'Latin1_General_BIN2'))
    UPDDAT_0: Mapped[datetime.datetime] = mapped_column(DateTime)
    DOCTYP_0: Mapped[int] = mapped_column(SmallInteger)
    BPPFLG_0: Mapped[int] = mapped_column(TINYINT)
    CREDATTIM_0: Mapped[datetime.datetime] = mapped_column(DateTime)
    UPDDATTIM_0: Mapped[datetime.datetime] = mapped_column(DateTime)
    AUUID_0: Mapped[bytes] = mapped_column(BINARY(16))
    CPYREL_0: Mapped[int] = mapped_column(TINYINT)
    CSLBPR_0: Mapped[str] = mapped_column(Unicode(1, 'Latin1_General_BIN2'))
    REGNUM_0: Mapped[str] = mapped_column(Unicode(1, 'Latin1_General_BIN2'))
    VATNO_0: Mapped[str] = mapped_column(Unicode(1, 'Latin1_General_BIN2'))
    ZPAGITM_0: Mapped[int] = mapped_column(TINYINT)
    EORINUM_0: Mapped[str] = mapped_column(Unicode(35, 'Latin1_General_BIN2'))
    INTSRVCOD_0: Mapped[str] = mapped_column(Unicode(1, 'Latin1_General_BIN2'))
    ZEDITOR_0: Mapped[int] = mapped_column(TINYINT)
    RTGCOD_0: Mapped[str] = mapped_column(Unicode(1, 'Latin1_General_BIN2'))
    EINVTYP_0: Mapped[int] = mapped_column(SmallInteger)
    ZINTVSP_0: Mapped[int] = mapped_column(TINYINT)
    MAPCOD_0: Mapped[str] = mapped_column(Unicode(1, 'Latin1_General_BIN2'))
    ZAGENTE_0: Mapped[int] = mapped_column(TINYINT)
    ZGESFLG_0: Mapped[int] = mapped_column(TINYINT)
    ZANAFLG_0: Mapped[int] = mapped_column(TINYINT)
    ZEXPFLG_0: Mapped[int] = mapped_column(TINYINT)
    ROWID: Mapped[decimal.Decimal] = mapped_column(
        Numeric(38, 0),
        Identity(start=decimal.Decimal('1'), increment=decimal.Decimal('1')),
        primary_key=True,
    )
