from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from decimal import Decimal
from typing import Optional, TYPE_CHECKING
from .tipo_reparacionEstado_schema import TipoReparacionEstado
from .taller_schema import Taller

if TYPE_CHECKING:
    from .vehiculo_schema import Vehiculo
    from .tipo_reparacionEstado_schema import TipoReparacionEstado
    from .taller_schema import Taller

class ReparacionBase(BaseModel):
    fecha: Optional[date] = None
    factura: Optional[str] = None
    fecha_pres: Optional[date] = None
    detalle: Optional[str] = None
    importe:  Optional[Decimal] = None
    caract: Optional[str] = None
    expediente: Optional[str] = None
    anioexp: Optional[int] = None
    alcance: Optional[str] = None
    nrocuerpo: Optional[str] = None
    km: Optional[int] = None
    vehiculo_id: int 
    tipo_reparacion_estado_id: Optional[int] = None
    taller_id: Optional[int] = None

class ReparacionCreate(ReparacionBase):
    pass

class ReparacionUpdate(BaseModel):
    fecha: Optional[date] = None
    factura: Optional[str] = None
    fecha_pres: Optional[date] = None
    detalle: Optional[str] = None
    importe:  Optional[Decimal] = None
    caract: Optional[str] = None
    expediente: Optional[str] = None
    anioexp: Optional[int] = None
    alcance: Optional[str] = None
    nrocuerpo: Optional[str] = None
    km: Optional[int] = None
    vehiculo_id: Optional[int] = None 
    tipo_reparacion_estado_id: Optional[int] = None
    taller_id: Optional[int] = None

class Reparacion(ReparacionBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    # Referencias en string, las clases se resolverán con model_rebuild()
    vehiculo: Optional["Vehiculo"] = None
    taller: Optional[Taller] = None
    tipo_reparacion_estado: Optional["TipoReparacionEstado"] = None

    model_config = ConfigDict(from_attributes=True)