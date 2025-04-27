from typing import List, Type, Union

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlmodel import SQLModel

from app.core.settings import DB_CONNECTION_STRING

# engine = create_engine(settings.DB_CONNECTION_STRING)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class DatabaseSession:
    """Database session manager."""

    def __init__(self, url: str = DB_CONNECTION_STRING):
        """Initialize the database session manager."""
        self.engine = create_engine(url, echo=True)
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
        )

    # close connection
    def close(self):
        self.engine.dispose()

    def create_tables(self, models: Union[Type[SQLModel], List[Type[SQLModel]]]):
        if not isinstance(models, list):
            models = [models]

        with self.engine.begin() as conn:
            for model in models:
                model.__table__.create(bind=conn, checkfirst=True)

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def commit_rollback(self, session: Session):  # noqa: PLR6301
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise


db = DatabaseSession()

# def get_db() -> Session:  # type: ignore
#     """Get a synchronous database session."""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# from sqlalchemy.ext.io import AsyncSession, async_sessionmaker, create_async_engine

# from app.core import settings

# engine = create_async_engine(settings.DB_CONNECTION_STRING)

# AsyncSessionLocal = async_sessionmaker(
#     bind=engine,
#     class_=AsyncSession,
#     expire_on_commit=False,
#     autocommit=False,
#     autoflush=False,
# )


# async def get_async_db() -> AsyncSession:  # type: ignore
#     """Get an asynchronous database session."""
#     async with AsyncSessionLocal() as session:
#         try:
#             yield session
#         except Exception:
#             raise
