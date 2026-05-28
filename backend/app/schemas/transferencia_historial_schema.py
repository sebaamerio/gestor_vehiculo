from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, TYPE_CHECKING

class TransferenciaHistorialBase(BaseModel):
    ro: int
    fecha: date
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    anio: Optional[str] = None
    dependencia_anterior_id: Optional[int] = None
    dependencia_id: Optional[int] = None

class Transferencia(TransferenciaHistorialBase):
    id: int

    model_config = ConfigDict(from_attributes=True)