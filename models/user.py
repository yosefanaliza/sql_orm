from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime, timezone


class User(SQLModel, table=True):
    """User model for CRUD operations"""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(unique=True, index=True)
    age: Optional[int] = None
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
