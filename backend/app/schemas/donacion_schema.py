from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, TYPE_CHECKING
from .tipo_acto_schema import TipoActoBase 
from .dependencia_schema import DependenciaBase
from .localidad_schema import LocalidadBase

# Necesario para evitar ciclo con Novedad
if TYPE_CHECKING:
    from .novedad_schema import Novedad 

class DonacionBase(BaseModel):
    fecha: date
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    dependencia_anterior_id: Optional[int] = None
    dependencia_anterior_descripcion: Optional[str] = None
    destino: Optional[str] = None
    localidad_id: Optional[int] = None
    fecha_resolucion: Optional[date] = None
    fecha_entrega: Optional[date] = None
    fecha_formulario: Optional[date] = None
    fecha_finalizado: Optional[date] = None

class DonacionCreate(DonacionBase):
    novedad_id: Optional[int] = None

class DonacionUpdate(BaseModel):
    fecha: Optional[date] = None
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    dependencia_anterior_id: Optional[int] = None
    dependencia_anterior_descripcion: Optional[str] = None
    destino: Optional[str] = None
    localidad_id: Optional[int] = None  
    fecha_resolucion: Optional[date] = None  
    fecha_entrega: Optional[date] = None
    fecha_formulario: Optional[date] = None
    fecha_finalizado: Optional[date] = None
    observaciones: Optional[str] = None
class Donacion(DonacionBase):
    id: int
    novedad_id: Optional[int] = None
    tipo_acto: Optional[TipoActoBase] = None
    dependencia_anterior_id: Optional[int] = None
    dependencia_anterior_descripcion: Optional[str] = None
    localidad: Optional[LocalidadBase] = None 

    
    model_config = ConfigDict(from_attributes=True)