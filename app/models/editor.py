from sqlalchemy import Index, PrimaryKeyConstraint, Unicode, text
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.database.mixins import (
    AuditMixin,
    PrimaryKeyMixin,
)


class Editor(Base, AuditMixin, PrimaryKeyMixin):
    __tablename__ = 'ZREDEXP'
    __table_args__ = (
        PrimaryKeyConstraint('ROWID', name='ZREDEXP_ROWID'),
        Index('ZREDEXP_ZRDX0', 'REDNUM_0', unique=True),
    )

    editor_id: Mapped[str] = mapped_column('REDNUM_0', Unicode(4, 'Latin1_General_BIN2'), default=text("''"))
    name: Mapped[str] = mapped_column('REDNAM_0', Unicode(35, 'Latin1_General_BIN2'), default=text("''"))
    contact: Mapped[str] = mapped_column('REDCNT_0', Unicode(35, 'Latin1_General_BIN2'), default=text("''"))
    email: Mapped[str] = mapped_column('REDMAI_0', Unicode(80, 'Latin1_General_BIN2'), default=text("''"))
    is_active: Mapped[int] = mapped_column('ENAFLG_0', TINYINT, default=text('2'))
