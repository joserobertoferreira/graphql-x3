from email_validator import EmailNotValidError, validate_email


class EmailResponse:
    """
    Represents the response of an email validation.
    """

    def __init__(self, ok: bool, message: str, normalize_email: str = None):
        self.ok = ok
        self.message = message
        self.normalize_email = normalize_email


class EmailValidation:
    """
    Validates an email address using the email-validator library.
    """

    def __init__(self, email: str):
        self.email = email

    def normalize_email(self) -> EmailResponse:
        try:
            resultado = validate_email(self.email, check_deliverability=False)
            return EmailResponse(ok=True, message='email', normalize_email=resultado.email)
        except EmailNotValidError as e:
            return EmailResponse(ok=False, message=str(e), normalize_email=None)
