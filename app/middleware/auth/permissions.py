from typing import Any

from strawberry.permission import BasePermission
from strawberry.types import Info

from app.middleware.auth.manager import JWTManager


class IsAuthenticated(BasePermission):
    message = 'User is not authenticated'

    def has_permission(self, source: Any, info: Info, **kwargs) -> bool:  # noqa: PLR6301
        request = info.context.get('request')

        # Access headers authentication
        authentication = request.headers.get('authentication')

        if authentication:
            token = authentication.split('Bearer ')[-1]
            return JWTManager.verify_token(token)

        return False
