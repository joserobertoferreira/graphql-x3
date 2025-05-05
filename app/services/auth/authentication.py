import datetime

from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from app.core import settings
from app.graphql.types.user import LoginInput, LoginType, RegisterInput, UserType
from app.middleware.auth.manager import JWTManager
from app.middleware.auth.validation import PasswordValidationError, PasswordValidatorService
from app.models.user import User
from app.repository.user import UserRepository


class AuthenticationService:
    """
    Authentication service for handling user login and registration.
    """

    # Password hashing context
    pwd_context = PasswordHash.recommended()

    @staticmethod
    def login(db: Session, login_data: LoginInput):
        user_ok = UserRepository.get_by_username_email(db, login_data.username, None)

        if user_ok:
            hash = AuthenticationService.pwd_context.hash(login_data.password)
            password_ok = AuthenticationService.pwd_context.verify(login_data.password, hash)

        if not user_ok or not password_ok:
            raise ValueError('Invalid username or password')

        payload = {'username': user_ok.username, 'password': hash}

        token = JWTManager.create_access_token(data=payload)

        return LoginType(username=user_ok.username, token=token)

    @staticmethod
    def register(db: Session, register_data: RegisterInput):
        """
        Registers a new user in the system.
        :param db: Database session
        :param register_data: Registration data containing username, email, and password
        :return: UserType object containing user information
        """
        # Check if username or email already exists
        user_exists = UserRepository.get_by_username_email(db, register_data.username, register_data.email)

        if user_exists:
            raise ValueError('Username or email already exists')

        # Check if password is valid and strong enough
        if not register_data.password:
            raise ValueError('Password is required')

        validator = PasswordValidatorService()

        is_valid, warning = validator.validate_username(register_data.username)

        if not is_valid:
            raise PasswordValidationError(
                message='Username does not meet complexity requirements',
                field=warning,
            )

        if validator.is_password_similar_to_username(password=register_data.password, username=register_data.username):
            raise ValueError('Password is too similar to username')

        is_valid, suggestions, warning = validator.validate_password(register_data.password)

        if not is_valid:
            raise PasswordValidationError(
                message='Password does not meet complexity requirements',
                field=suggestions,
                details=warning,
            )

        user = User()
        user.username = register_data.username
        user.email = register_data.email
        user.is_active = register_data.is_active
        user.is_superuser = False
        user.date_joined = datetime.date.today()
        user.last_login = settings.DEFAULT_LEGACY_DATETIME
        user.password = AuthenticationService.pwd_context.hash(register_data.password)

        new_user = UserRepository.create_user(db, user)

        return UserType(
            user_id=new_user.id,
            username=new_user.username,
            email=new_user.email,
            date_joined=new_user.date_joined,
            last_login=new_user.last_login,
            is_active=new_user.is_active,
            is_superuser=new_user.is_superuser,
        )
