from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, TYPE_CHECKING
from .tipo_acto_schema import TipoActoBase 
from .dependencia_schema import DependenciaBase
from .localidad_schema import LocalidadBase

# Necesario para evitar ciclo con Novedad
if TYPE_CHECKING:
    from .novedad_schema import Novedad 

class ComodatoBase(BaseModel):
    fecha: date
    dependencia_id: Optional[int] = None
    dependencia_descripcion: Optional[str] = None
    fecha_fin: Optional[date] = None  
    destino: Optional[str] = None
    expediente: Optional[str] = None
    informe: Optional[str] = None
    localidad_id: Optional[int] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None

class ComodatoCreate(ComodatoBase):
    novedad_id: Optional[int] = None

class ComodatoUpdate(BaseModel):
    fecha: date
    dependencia_id: Optional[int] = None
    dependencia_descripcion: Optional[str] = None
    fecha_fin: Optional[date] = None  
    destino: Optional[str] = None
    expediente: Optional[str] = None
    informe: Optional[str] = None
    localidad_id: Optional[int] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    observaciones: Optional[str] = None

class Comodato(ComodatoBase):
    id: int
    novedad_id: Optional[int] = None
    tipo_acto: Optional[TipoActoBase] = None
    dependencia_id: Optional[int] = None
    dependencia_descripcion: Optional[str] = None
    localidad: Optional[LocalidadBase] = None

    
    model_config = ConfigDict(from_attributes=True)