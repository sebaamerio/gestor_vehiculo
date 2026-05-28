from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, TYPE_CHECKING
from .tipo_acto_schema import TipoActoBase 

# Necesario para evitar ciclo con Novedad
if TYPE_CHECKING:
    from .novedad_schema import Novedad 

class CambioChasisBase(BaseModel):
    chasis_anterior: str
    chasis_nuevo: str
    fecha: date
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None

class CambioChasisCreate(CambioChasisBase):
    novedad_id: Optional[int] = None

class CambioChasisUpdate(BaseModel):
    chasis_anterior: Optional[str] = None
    chasis_nuevo: Optional[str] = None
    fecha: Optional[date] = None
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    observaciones: Optional[str] = None
    
class CambioChasis(CambioChasisBase):
    id: int
    novedad_id: Optional[int] = None
    tipo_acto: Optional[TipoActoBase] = None
    
    model_config = ConfigDict(from_attributes=True)