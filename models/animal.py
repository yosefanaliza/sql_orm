from typing import Optional
from sqlmodel import Field, SQLModel


class Animal(SQLModel, table=True):
    """Animal model for CRUD operations"""

    id: Optional[int] = Field(default=None, primary_key=True)
    species: str = Field(index=True)
    name: str = Field(index=True)
    age: Optional[int] = None
    is_domestic: bool = Field(default=True)
