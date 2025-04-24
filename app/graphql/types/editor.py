from typing import Optional

import strawberry

ACTIVE = 2


@strawberry.type
class EditorType:
    editor_id: str
    name: str
    contact: Optional[str]
    email: Optional[str]
    is_active: Optional[int]


@strawberry.input
class EditorInput:
    name: str
    contact: Optional[str] = None
    email: Optional[str] = None
    is_active: int = ACTIVE
