from pydantic import BaseModel, Field, field_validator
from uuid import UUID, uuid4

class Medicamento(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nome: str = Field(..., min_length=2)
    dosagem: str
    estoque: int

    @field_validator('estoque')
    @classmethod
    def estoque_positivo(cls, v: int):
        if v < 0:
            raise ValueError('O estoque não pode ser negativo')
        return v