from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, TYPE_CHECKING
from .tipo_acto_schema import TipoActoBase 

# Necesario para evitar ciclo con Novedad
if TYPE_CHECKING:
    from .novedad_schema import Novedad 

class BajaBase(BaseModel):
    fecha: date
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None

class BajaCreate(BajaBase):
    novedad_id: Optional[int] = None 

class BajaUpdate(BaseModel):
    fecha: Optional[date] = None 
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    observaciones: Optional[str] = None
    
class Baja(BajaBase):
    id: Optional[int] = None
    novedad_id: Optional[int] = None
    tipo_acto: Optional[TipoActoBase] = None
    
    model_config = ConfigDict(from_attributes=True)