import strawberry


@strawberry.type
class EmailResponseType:
    ok: bool
    message: str
    normalize_email: str | None = None
