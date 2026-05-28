from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, TYPE_CHECKING
from .tipo_acto_schema import TipoActoBase 
from .chofer_schema import ChoferBase
from .localidad_schema import LocalidadBase

# Necesario para evitar ciclo con Novedad
if TYPE_CHECKING:
    from .novedad_schema import Novedad 

class RoboBase(BaseModel):
    fecha: date
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    chofer_id: Optional[int] = None
    localidad_id: Optional[int] = None
    fecha_recupero: Optional[date] = None   

class RoboCreate(RoboBase):
    novedad_id: Optional[int] = None 

class RoboUpdate(BaseModel):
    fecha: Optional[date] = None   
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    chofer_id: Optional[int] = None
    localidad_id: Optional[int] = None
    fecha_recupero: Optional[date] = None
    observaciones: Optional[str] = None    
class Robo(RoboBase):
    id: int
    novedad_id: Optional[int] = None 
    tipo_acto: Optional[TipoActoBase] = None
    chofer: Optional[ChoferBase] = None 
    localidad: Optional[LocalidadBase] = None 

    
    model_config = ConfigDict(from_attributes=True)