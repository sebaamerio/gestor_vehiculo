from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, TYPE_CHECKING
from .tipo_acto_schema import TipoActoBase 

# Necesario para evitar ciclo con Novedad
if TYPE_CHECKING:
    from .novedad_schema import Novedad 

class CambioMotorBase(BaseModel):
    motor_nro_anterior: str
    motor_nro_nuevo: str
    fecha: date
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None

class CambioMotorCreate(CambioMotorBase):
    novedad_id: Optional[int] = None

class CambioMotorUpdate(BaseModel):
    motor_nro_anterior: Optional[str] = None
    motor_nro_nuevo: Optional[str] = None
    fecha: Optional[date] = None
    expediente: Optional[str] = None
    informe: Optional[str] = None
    acto_id: Optional[int] = None
    norma: Optional[str] = None
    observaciones: Optional[str] = None
    
class CambioMotor(CambioMotorBase):
    id: int
    novedad_id: Optional[int] = None
    tipo_acto: Optional[TipoActoBase] = None
    
    model_config = ConfigDict(from_attributes=True)