from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, TYPE_CHECKING
from .tipo_acto_schema import TipoActoBase 
from .dependencia_schema import DependenciaBase

# Necesario para evitar ciclo con Novedad
if TYPE_CHECKING:
    from .novedad_schema import Novedad 

class TransferenciaBase(BaseModel):
    fecha: date
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    dependencia_anterior_id: Optional[int] = None
    dependencia_id: Optional[int] = None
    dependencia_anterior_descripcion: Optional[str] = None
    dependencia_descripcion: Optional[str] = None
class TransferenciaCreate(TransferenciaBase):
    novedad_id: Optional[int] = None

class TransferenciaUpdate(BaseModel):
    fecha: Optional[date] = None
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    dependencia_anterior_id: Optional[int] = None
    dependencia_id: Optional[int] = None
    observaciones: Optional[str] = None
    dependencia_anterior_descripcion: Optional[str] = None
    dependencia_descripcion: Optional[str] = None
    
class Transferencia(TransferenciaBase):
    id: int
    novedad_id: Optional[int] = None
    tipo_acto: Optional[TipoActoBase] = None
    dendencia_anterior: Optional[DependenciaBase] = None 
    dendencia: Optional[DependenciaBase] = None
    dependencia_anterior_descripcion: Optional[str] = None
    dependencia_descripcion: Optional[str] = None


    model_config = ConfigDict(from_attributes=True)