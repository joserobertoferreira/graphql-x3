import difflib
import re
from typing import Optional

from password_validator import PasswordValidator
from zxcvbn import zxcvbn

from app.core.settings import (
    LITERAL_THREE,
    PASSWORD_MAX_LENGTH,
    PASSWORD_MIN_LENGTH,
    USERNAME_MAX_LENGTH,
    USERNAME_MIN_LENGTH,
)


class PasswordValidatorService:
    """
    Service for validating passwords.
    """

    def __init__(self):
        self.schema = PasswordValidator()
        (
            self.schema.min(PASSWORD_MIN_LENGTH)
            .max(PASSWORD_MAX_LENGTH)
            .has()
            .uppercase()
            .has()
            .lowercase()
            .has()
            .digits()
            .has()
            .symbols()
            .has()
            .no()
            .spaces()
        )

    def validate_password(self, password: str) -> tuple[bool, list, str]:
        """
        Validate the password against the defined rules.
        """

        failed_rules = {
            'min_length': f'Password must be at least {PASSWORD_MIN_LENGTH} characters long',
            'max_length': f'Password must be at most {PASSWORD_MAX_LENGTH} characters long',
            'uppercase': 'Password must contain at least one uppercase letter',
            'lowercase': 'Password must contain at least one lowercase letter',
            'digits': 'Password must contain at least one digit',
            'symbols': 'Password must contain at least one symbol',
            'spaces': 'Password must not contain spaces',
        }

        if not self.schema.validate(password):
            return False, failed_rules, 'Password validation failed'

        # Check password strength using zxcvbn
        result = zxcvbn(password)

        if result['score'] < LITERAL_THREE:
            print(f'Password strength is weak: {result}')
            warning = 'Password is too weak'
            suggestions = []

            if 'feedback' in result:
                if result['feedback']['warning']:
                    warning = result['feedback']['warning']

                if result['feedback']['suggestions']:
                    suggestions = result['feedback']['suggestions']

            return False, suggestions, warning

        return True, [], ''

    def validate_username(self, username: str) -> tuple[bool, str]:  # noqa: PLR6301
        """
        Validate the username against the defined rules.
        """
        username = username.lower()

        # Check if username is empty
        if not username:
            return False, 'Username cannot be empty.'

        # Check if username is too short or too long
        if len(username) < USERNAME_MIN_LENGTH:
            return False, f'The username must be at least {USERNAME_MIN_LENGTH} characters long.'
        if len(username) > USERNAME_MAX_LENGTH:
            return False, f'The username must be at most {USERNAME_MAX_LENGTH} characters long.'

        # Check if starts with a letter
        if not username[0].isalpha():
            return False, 'Username must start with a letter.'

        # check if contains only letters and numbers
        if not re.fullmatch(r'[a-z0-9]+', username):
            return False, 'Username can only contain letters and numbers.'

        return True, ''

    def is_password_similar_to_username(  # noqa: PLR6301
        self, password: Optional[str], username: Optional[str], threshold: float = 0.7
    ) -> bool:
        """
        Checks if the password is considered too similar to the username,
        based on a similarity threshold.

        Args:
            password: The password to be checked.
            username: The username for comparison.
            threshold: The similarity ratio (between 0.0 and 1.0) above which
                 the password is considered too similar. Defaults to 0.7.

        Returns:
            True if the similarity is GREATER than the threshold, False otherwise.

        Raises:
            ValueError: If the threshold is outside the range [0.0, 1.0].
        """

        # check if threshold is between 0.0 and 1.0
        if not (0.0 <= threshold <= 1.0):
            raise ValueError('Threshold must be between 0.0 and 1.0')

        # Handles cases of None or empty strings (cannot be similar)
        if not password or not username:
            return False

        pwd_lower = str(password).lower()
        usr_lower = str(username).lower()

        # Calculate the similarity ratio
        # The first argument 'None' specifies not to worry about "junk characters"
        matcher = difflib.SequenceMatcher(None, pwd_lower, usr_lower)
        similarity_ratio = matcher.ratio()

        # Debug (opcional)
        print(f"DEBUG: Similarity between '{password}' and '{username}': {similarity_ratio:.2f}")

        # Check if the ratio exceeds the threshold
        return similarity_ratio > threshold


class PasswordValidationError(ValueError):
    def __init__(self, message: str, code: str = None, field: str = None, details: dict = None):
        super().__init__(message)

        self.code = code
        self.field = field
        self.details = details or {}

    # Opcional: Sobrescrever __str__ para uma melhor representação
    def __str__(self) -> str:
        base_message = super().__str__()  # Pega a mensagem passada para o ValueError
        parts = []
        if self.code:
            parts.append(f'Code: {self.code}')
        if self.field:
            parts.append(f'Field: {self.field}')
        if parts:
            return f'{base_message} ({", ".join(parts)})'
        return base_message
