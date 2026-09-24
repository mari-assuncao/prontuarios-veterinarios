from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship


class VeterinarioBase(SQLModel):
    nome: str = Field(min_length=3, max_length=120, index=True)
    crmv: str = Field(min_length=8, unique=True, index=True)
    email: str | None = Field(default=None, max_length=120, unique=True)
    telefone: str | None = Field(default=None, max_length=20)
    ativo: bool = True