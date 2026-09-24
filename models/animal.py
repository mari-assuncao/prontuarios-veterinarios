from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

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
    especie: Especie = Field(default=None, index=True)
    raca: str = Field(min_length=2, max_length=50, index=True)
    sexo: Sexo = Field(sa_column=Column(String(1), index=True)) # reposta so pode haver um caractere
    ano_nascimento: int | None = Field(default=None, ge=2000) # ano precisa ser maior ou igual a 1900
    peso: float = Field(gt=0, le=200) # peso precisa ser maior que 0 e menor que 200
    porte: Porte = Field(default=None, min_length=1, max_length=10)
    observacoes: str | None = None
    ativo: bool = True

class Animal(AnimalBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # fzr relacionamento com tutor, vet e consulta

class AnimalCreate(AnimalBase):
    pass

class AnimalPublic(AnimalBase):
    id: int

class AnimalUpdate(AnimalBase):
    nome: str | None = Field(min_length=3, max_length=50)
    especie: Especie | None = None
    raca: str | None = Field(min_length=2, max_length=50)
    sexo: Sexo | None = Field(sa_column=Column(String(1))) # reposta so pode haver um caractere
    ano_nascimento: int | None = Field(default=None, ge=1900) # ano precisa ser maior ou igual a 1900
    peso: float | None = Field(gt=0, le=200) # peso precisa ser maior que 0 e menor que 200
    porte: Porte | None = None
    observacoes: str | None = None
    ativo: bool | None = None
