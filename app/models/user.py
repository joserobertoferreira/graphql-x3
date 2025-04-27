import datetime
from typing import Optional

from sqlalchemy import BigInteger, Boolean, Date, Identity, Index, PrimaryKeyConstraint, Unicode
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='PK__users__3213E83F4E0081C0'),
        Index('UQ__users__AB6E6164B3A0AE1E', 'email', unique=True),
        Index('UQ__users__F3DBC572B471A1B8', 'username', unique=True),
        {'schema': 'dbo'},
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1), primary_key=True)
    password: Mapped[str] = mapped_column(Unicode(128, 'Latin1_General_BIN2'))
    is_superuser: Mapped[bool] = mapped_column(Boolean)
    email: Mapped[str] = mapped_column(Unicode(254, 'Latin1_General_BIN2'))
    is_active: Mapped[bool] = mapped_column(Boolean)
    date_joined: Mapped[datetime.date] = mapped_column(Date)
    username: Mapped[str] = mapped_column(Unicode(20, 'Latin1_General_BIN2'))
    last_login: Mapped[Optional[datetime.datetime]] = mapped_column(DATETIME2)
