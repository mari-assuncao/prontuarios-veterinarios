from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship


class TutorBase(SQLModel):
    nome: str = Field(min_length=3, max_length=120, index=True)
    cpf: str = Field(sa_column=Column(String(14)), unique=True, nullable=False, index=True)
    telefone: str = Field(default=None, max_length=18)
    email: str | None = Field(default=None, max_length=120, unique=True)
    ativo: bool = True

class Tutor(TutorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # fzr relacionamento

class TutorCreate(TutorBase):
    pass

class TutorPublic(TutorBase):
    id: int

class TutorUpdate(SQLModel):
    nome: str | None = Field(default=None, min_length=3, max_length=120, index=True)
    # atualiza pegando o cpf
    cpf: str = Field(sa_column=Column(String(14)), unique=True, nullable=False, index=True) 
    telefone: str | None = Field(default=None, max_length=18)
    email: str | None = Field(default=None, max_length=120, unique=True)
    ativo: bool | None = True