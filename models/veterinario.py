from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship

from models import Especialidade


class VeterinarioBase(SQLModel):
    nome: str = Field(min_length=3, max_length=120, index=True)
    crmv: str = Field(sa_column=Column(String(30)), unique=True, nullable=False, index=True)
    email: str | None = Field(default=None, max_length=120, unique=True)
    telefone: str | None = Field(default=None, max_length=20)
    ativo: bool = True

class Veterinario(VeterinarioBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # fzr relacionamento
 
class VeterinarioCreate(VeterinarioBase):
    especialidade_ids: list[int] = [] 

class VeterinarioPublic(VeterinarioBase):
    id: int
    
class VeterinarioPublicDetalhado(VeterinarioPublic):
    especialidade: list[EspecialidadePublic] = []
    
class VeterinarioUpdate(SQLModel):
    nome: str | None = None
    crmv: str | None = None
    email: str | None = None
    telefone: str | None = None
    ativo: bool | None = None
    especialidade_ids: list[int] | None = None