from datetime import date, datetime
from enum import Enum
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship

from models import Animal, Veterinario, Especialidade

class StatusConsulta(str, Enum):
    AGENDADA = "agendada"
    CONFIRMADA = "confirmada"
    REALIZADA = "realizada"
    CANCELADA = "cancelada"

class ConsultaBase(SQLModel):
    animal_id: int = Field(foreign_key="animal.id", index=True)
    veterinario_id: int = Field(foreign_key="veterinario.id", index=True)
    especialidade_id: int = Field(foreign_key="especialidade.id", index=True)
    
    data_hora: datetime = Field(index=True)
    status: StatusConsulta = Field(default=StatusConsulta.AGENDADA, index=True)
    motivo: str = Field(min_length=3, max_length=300)
    observacoes: str | None = Field(default=None, min_length=3, max_length=1000)
    valor: float = Field(default=0, ge=0) #valor precisa ser maior que 0

class Consulta(ConsultaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # relacionamento
    animal: Animal | None = Relationship(back_populates="consultas")
    veterinario: Veterinario | None = Relationship(back_populates="consultas")
    especialidade: Especialidade | None = Relationship(back_populates="consultas")

class ConsultaCreate(ConsultaBase):
    pass 

class ConsultaPublic(ConsultaBase):
    id: int
    
class ConsultaPublicDetalhada(ConsultaPublic):
    animal: AnimalPublic | None = None
    veterinario: VeterinarioPublic | None = None
    especialidade: EspecialidadePublic | None = None
    
class ConsultaUpdate(SQLModel):
    animal_id: int | None = None
    veterinario_id: int | None = None
    especialidade_id: int | None = None
    data_hora: datetime | None = None
    status: StatusConsulta | None = None
    motivo: str | None = None
    observacoes: str | None = None
    valor: float | None = None