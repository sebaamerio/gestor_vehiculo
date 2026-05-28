from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from typing import Optional, TYPE_CHECKING, List
from .tipo_vtvResultado_schema import TipoVtvResultadoSinVtv
# ⚠️ CLAVE: NO IMPORTAMOS Vehiculo AQUÍ. Usamos la referencia en string.
# (TipoVtvResultado ya debería estar importado en TipoVtvResultadoBase o su propio esquema)
if TYPE_CHECKING:
    from .vehiculo_schema import Vehiculo
    from .tipo_vtvResultado_schema import TipoVtvResultado

class VtvBase(BaseModel):
    fecha_solicitud: Optional[date] = None
    fecha_realizada: Optional[date] = None
    fecha_vto: Optional[date] = None
    zona: Optional[int] = None
    oblea: Optional[str] = None
    observaciones: Optional[str] = None
    vehiculo_id: int 
    tipo_vtvResultado_id: Optional[int] = None

class VtvCreate(VtvBase):
    pass

class VtvUpdate(BaseModel):
    fecha_solicitud: Optional[date] = None
    fecha_realizada: Optional[date] = None
    fecha_vto: Optional[date] = None
    zona: Optional[int] = None
    oblea: Optional[str] = None
    observaciones: Optional[str] = None
    tipo_vtvResultado_id: Optional[int] = None
    vehiculo_id: Optional[int] = None
class Vtv(VtvBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    # Referencias en string, las clases se resolverán con model_rebuild()
    vehiculo: Optional["Vehiculo"] = None 
    tipo_vtvResultado: Optional[TipoVtvResultadoSinVtv] = None # Usar cadena si TipoVtvResultado no se importa directamente.

    model_config = ConfigDict(from_attributes=True)

class VtvPaginated(BaseModel):
    total: int
    data: List[Vtv]
class vtvVencida(BaseModel):   
    value: int
    
# ⚠️ No se necesita model_rebuild() aquí.