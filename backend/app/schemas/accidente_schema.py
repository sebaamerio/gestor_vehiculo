from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, TYPE_CHECKING
from .tipo_acto_schema import TipoActoBase 
from .chofer_schema import ChoferBase
from .localidad_schema import LocalidadBase

# Necesario para evitar ciclo con Novedad
if TYPE_CHECKING:
    from .novedad_schema import Novedad 

class AccidenteBase(BaseModel):
    fecha: date
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    chofer_id: Optional[int] = None
    localidad_id: Optional[int] = None
    fecha_inicio_sumario: Optional[date] = None
    fecha_fin_sumario: Optional[date] = None
    lugar: Optional[str] = None

class AccidenteCreate(AccidenteBase):
    novedad_id: Optional[int] = None

class AccidenteUpdate(BaseModel):
    fecha: Optional[date] = None   
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    chofer_id: Optional[int] = None
    localidad_id: Optional[int] = None
    fecha_inicio_sumario: Optional[date] = None
    fecha_fin_sumario: Optional[date] = None
    lugar: Optional[str] = None
    observaciones: Optional[str] = None
    
class Accidente(AccidenteBase):
    id: int
    novedad_id: Optional[int] = None
    tipo_acto: Optional[TipoActoBase] = None
    chofer: Optional[ChoferBase] = None 
    localidad: Optional[LocalidadBase] = None 

    
    model_config = ConfigDict(from_attributes=True)