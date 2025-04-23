from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core import settings

engine = create_engine(settings.DB_CONNECTION_STRING)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:  # type: ignore
    """Get a synchronous database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

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
