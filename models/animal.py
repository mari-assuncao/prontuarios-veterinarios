from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

if TYPE_CHECKING:
    from models.consulta import Consulta
    from models.tutor import Tutor

#enum
class Sexo(str, Enum):
    MASCULINO = "M"
    FEMININO = "F"

class Especie(str, Enum):
    GATO = "gato"
    CACHORRO = "cachorro"
    AVE = "ave"
    REPTIL = "reptil"

class Porte(str, Enum):
    PEQUENO = "pequeno"
    MEDIO = "medio"
    GRANDE = "grande"


class AnimalBase(SQLModel):
    nome: str = Field(min_length=3, max_length=50, index=True)
    especie: Especie = Field(index=True)
    raca: str = Field(min_length=2, max_length=50, index=True)
    sexo: Sexo
    ano_nascimento: int | None = Field(default=None, ge=1900) # ano precisa ser maior ou igual a 1900
    peso: float = Field(gt=0, le=200) # peso precisa ser maior que 0 e menor que 200
    porte: Porte | None = None
    observacoes: str | None = None
    ativo: bool = True
    tutor_id: int = Field(foreign_key="tutor.id", index=True)

class Animal(AnimalBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # relacionamento com tutor e consulta
    tutor: "Tutor" = Relationship(back_populates="animais")
    consultas: list["Consulta"] = Relationship(back_populates="animal")

class AnimalCreate(AnimalBase):
    pass

class AnimalPublic(AnimalBase):
    id: int

class AnimalUpdate(SQLModel):
    nome: str | None = Field(default=None, min_length=3, max_length=50)
    especie: Especie | None = None
    raca: str | None = Field(default=None, min_length=2, max_length=50)
    sexo: Sexo | None = None
    ano_nascimento: int | None = Field(default=None, ge=1900) # ano precisa ser maior ou igual a 1900
    peso: float | None = Field(default=None, gt=0, le=200) # peso precisa ser maior que 0 e menor que 200
    porte: Porte | None = None
    observacoes: str | None = None
    ativo: bool | None = None
    tutor_id: int | None = None
