import datetime
from typing import Optional

import strawberry


@strawberry.type
class UserType:
    user_id: str
    username: str
    email: Optional[str]
    date_joined: Optional[datetime.date]
    last_login: Optional[datetime.datetime]
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


@strawberry.type
class LoginType:
    username: str
    token: str


@strawberry.input
class RegisterInput:
    username: str
    email: str
    password: str
    is_active: Optional[bool] = True


@strawberry.input
class LoginInput:
    username: str
    password: str
