from typing import TYPE_CHECKING

from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.animal import Animal


class TutorBase(SQLModel):
    nome: str = Field(min_length=3, max_length=120, index=True)
    cpf: str = Field(sa_column=Column(String(14), unique=True, nullable=False, index=True))
    telefone: str | None = Field(default=None, max_length=18)
    email: str | None = Field(default=None, max_length=120, unique=True)
    ativo: bool = True

class Tutor(TutorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    animais: list["Animal"] = Relationship(back_populates="tutor")

class TutorCreate(TutorBase):
    pass

class TutorPublic(TutorBase):
    id: int

class TutorUpdate(SQLModel):
    nome: str | None = Field(default=None, min_length=3, max_length=120)
    cpf: str | None = Field(default=None, max_length=14)
    telefone: str | None = Field(default=None, max_length=18)
    email: str | None = Field(default=None, max_length=120)
    ativo: bool | None = None