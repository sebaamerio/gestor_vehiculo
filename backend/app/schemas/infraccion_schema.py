from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, TYPE_CHECKING
from .tipo_pago_schema import TipoPagoBase 
from .chofer_schema import ChoferBase
from .localidad_schema import LocalidadBase

# Necesario para evitar ciclo con Novedad
if TYPE_CHECKING:
    from .novedad_schema import Novedad 

class InfraccionBase(BaseModel):
    fecha: date
    chofer_id: Optional[int] = None
    localidad_id: Optional[int] = None    
    acta: Optional[str] = None
    citacion: Optional[str] = None
    causa: Optional[str] = None
    tipo_pago_id: Optional[int] = None

class InfraccionCreate(InfraccionBase):
    novedad_id: Optional[int] = None

class InfraccionUpdate(BaseModel):
    fecha: date
    chofer_id: Optional[int] = None
    localidad_id: Optional[int] = None    
    acta: Optional[str] = None
    citacion: Optional[str] = None
    causa: Optional[str] = None
    tipo_pago_id: Optional[int] = None
    observaciones: Optional[str] = None
    
class Infraccion(InfraccionBase):
    id: int
    novedad_id: Optional[int] = None
    tipo_pago: Optional[TipoPagoBase] = None
    chofer: Optional[ChoferBase] = None 
    localidad: Optional[LocalidadBase] = None 

    
    model_config = ConfigDict(from_attributes=True)