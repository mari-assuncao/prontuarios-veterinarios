from datetime import date, datetime
from enum import Enum
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship

class StatusConsulta(str, Enum):
    AGENDADA = "agendada"
    CONFIRMADA = "confirmada"
    REALIZADA = "realizada"
    CANCELADA = "cancelada"

