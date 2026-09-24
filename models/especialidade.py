from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship


class EspecialidadeBase(SQLModel):
    nome: str = Field(min_length=3, 
                      max_length=120, 
                      index=True, 
                      nullable=False, 
                      unique=True)
    descricao: str | None = Field(default=None, max_length=300)

class Especialidade(EspecialidadeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # fzr relacionamento com vet


class EspecialidadeCreate(EspecialidadeBase):
    pass

class EspecialidadePublic(EspecialidadeBase):
    id: int

class EspecialidadeUpdate(SQLModel):
    nome: str | None = None
    descricao: str | None = None