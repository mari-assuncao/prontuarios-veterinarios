from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

from models.veterinario_especialidade import VeterinarioEspecialidade

if TYPE_CHECKING:
    from models.veterinario import Veterinario
    from models.consulta import Consulta


class EspecialidadeBase(SQLModel):
    nome: str = Field(min_length=3, 
                      max_length=120, 
                      index=True, 
                      nullable=False, 
                      unique=True)
    descricao: str | None = Field(default=None, max_length=300)

class Especialidade(EspecialidadeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    veterinarios: list["Veterinario"] = Relationship(
        back_populates="especialidades",
        link_model=VeterinarioEspecialidade
    )
    consultas: list["Consulta"] = Relationship(back_populates="especialidade")


class EspecialidadeCreate(EspecialidadeBase):
    pass

class EspecialidadePublic(EspecialidadeBase):
    id: int

class EspecialidadeUpdate(SQLModel):
    nome: str | None = None
    descricao: str | None = None