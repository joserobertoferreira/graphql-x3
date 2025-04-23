from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from app.core.settings import DB_SCHEMA

metadata_obj = MetaData(schema=DB_SCHEMA)


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    This class uses a custom metadata object to set the schema for all models.
    """

    metadata = metadata_obj

    # @classmethod
    # def get_schema(cls) -> str:
    #     """
    #     Returns the schema name for the model.
    #     This method is used to set the schema for all models in the application.
    #     """
    #     return cls.metadata.schema
