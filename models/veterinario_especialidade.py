from sqlmodel import SQLModel, Field


# tabela de ligacao N:N entre veterinario e especialidade
class VeterinarioEspecialidade(SQLModel, table=True):
    veterinario_id: int | None = Field(default=None, foreign_key="veterinario.id", primary_key=True)
    especialidade_id: int | None = Field(default=None, foreign_key="especialidade.id", primary_key=True)
