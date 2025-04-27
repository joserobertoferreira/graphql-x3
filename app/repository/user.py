from typing import Optional

from sqlalchemy import delete as sql_delete
from sqlalchemy import update as sql_update
from sqlalchemy.orm import Session
from sqlalchemy.sql import or_, select

from app.database.database import db
from app.models.user import User


class UserRepository:
    @staticmethod
    def create_user(db: Session, user_data: User):
        """Create a new user in the database."""

        db.add(user_data)
        db.flush()
        db.commit()
        db.refresh(user_data)

        return user_data

    @staticmethod
    def update(user_id: int, user_data: User):
        with db as session:
            stmt = select(User).where(User.id == user_id)
            result = session.execute(stmt)

            user = result.scalars().first()
            user.email = user_data.email

            query = (
                sql_update(User)
                .where(User.id == user_id)
                .values(**User.dict())
                .execution_options(synchronize_session='fetch')
            )

            session.execute(query)
            db.commit_rollback()

    @staticmethod
    def delete(user_id: int):
        with db as session:
            query = sql_delete(User).where(User.id == user_id)
            session.execute(query)
            db.commit_rollback()

    @staticmethod
    def get_by_id(user_id: int) -> User:
        with db as session:
            stmt = select(User).where(User.id == user_id)
            result = session.execute(stmt)
            user = result.scalars().first()
            return user

    @staticmethod
    def get_all():
        with db as session:
            query = select(User)
            result = session.execute(query)
            return result.scalars().all()

    @staticmethod
    def get_by_username_email(db: Session, username: Optional[str], email: Optional[str]) -> User:
        """fetch user by username or email"""

        stmt = select(User).where(or_(User.username == username, User.email == email))
        result = db.execute(stmt)
        return result.scalars().first()
