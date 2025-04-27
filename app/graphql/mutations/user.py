import strawberry
from sqlalchemy.orm import Session
from strawberry.types import Info

from app.graphql.types.email import EmailResponseType
from app.graphql.types.user import LoginInput, LoginType, RegisterInput, UserType
from app.middleware.validators.email_validation import EmailResponse as EmailResponseInternal
from app.middleware.validators.email_validation import EmailValidation
from app.services.auth.authentication import AuthenticationService

ContextType = dict


def to_graphql_response(resp: EmailResponseInternal) -> EmailResponseType:
    return EmailResponseType(ok=resp.ok, message=resp.message, normalize_email=resp.normalize_email)


@strawberry.type
class UserMutation:
    """
    User mutation class for handling user-related operations.
    """

    @strawberry.field
    def login(self, info: Info[ContextType, None], login_data: LoginInput) -> LoginType:  # noqa: PLR6301
        """Attempts to log in a user and returns a token."""

        db: Session = info.context.get('db')

        if not db:
            raise ValueError('Sessão do banco de dados não encontrada.')

        try:
            login = AuthenticationService.login(db, login_data)
            return login
        except ValueError as e:
            raise ValueError(f'Erro ao processar o login: {e}') from e

    @strawberry.field
    def register(self, info: Info[ContextType, None], register_data: RegisterInput) -> UserType:  # noqa: PLR6301
        """Attempts to register a new user."""

        db: Session = info.context.get('db')

        if not db:
            raise ValueError('Sessão do banco de dados não encontrada.')

        # Validate email
        email_validation = EmailValidation(register_data.email).normalize_email()

        if not email_validation.ok:
            raise ValueError(to_graphql_response(email_validation))

        try:
            register = AuthenticationService.register(db, register_data)
            return register
        except ValueError as e:
            raise ValueError(f'Erro ao processar o registro: {e}') from e
