from typing import Optional
from sqlmodel import Field, SQLModel


class Car(SQLModel, table=True):
    """Car model for CRUD operations"""

    id: Optional[int] = Field(default=None, primary_key=True)
    make: str = Field(index=True)
    model: str = Field(index=True)
    year: int
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")
