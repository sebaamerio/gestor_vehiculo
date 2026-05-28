from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from datetime import date, datetime
from typing import Optional, List, TYPE_CHECKING

# Importaciones de otros esquemas base (NO CAUSAN EL CICLO)
from .vehiculo_dependencia_schema import VehiculoDependenciaBase
from .tipo_marca_schema import TipoMarcaBase
from .tipo_modelo_schema import TipoModeloBase
from .tipo_vehiculo_schema import TipoVehiculoBase
from .tipo_carroceria_schema import TipoCarroceria
from .tipo_motor_schema import TipoMotorBase
from .tipo_condicion_schema import TipoCondicionBase
from .tipo_situacion_schema import TipoSituacionBase

from .tipo_aptitud_schema import TipoAptitudBase
from .tipo_cabina_schema import TipoCabinaBase
from .tipo_traccion_schema import TipoTraccionBase


# ⚠️ CLAVE: NO IMPORTAMOS Vtv AQUÍ. Usamos la referencia en string.
if TYPE_CHECKING:
    from .vtv_schema import Vtv
    from .novedad_schema import Novedad

class VehiculoBase(BaseModel):
    registro_nro: Optional[int] = None
    registro_marca: bool
    fecha_titulo: Optional[date] = None
    marca_id: Optional[int] = None
    modelo_id: Optional[int] = None
    tipo_vehiculo_id: Optional[int] = None
    carroceria_id: Optional[int] = None
    anio: Optional[int] = None
    plazas: Optional[int] = None
    carga: Optional[int] = None
    tipo_motor_id: Optional[int] = None
    ejes: Optional[int] = None
    condicion_id: Optional[int] = None
    motor_marca: Optional[str] = None
    motor_nro: str
    dominio: Optional[str] = None
    dominio_anterior: Optional[str] = None
    chasis_marca: Optional[str] = None
    chasis_nro: str
    tipo_dominio: Optional[str] = None
    situacion_id: Optional[int] = None
    tipo_aptitud_id: Optional[int] = None
    tipo_cabina_id : Optional[int] = None
    tipo_traccion_id: Optional[int] = None
    fechaVtv: Optional[date] = None
    observaciones: Optional[str] = None
    update_user: Optional[str] = None
    origen: Optional[str] = None
    empresa: Optional[str] = None
    ri_anterior: Optional[int] = None
class VehiculoCreate(VehiculoBase):
    dominio: str
    dependencia_id: Optional[int] = None    

class VehiculoUpdate(BaseModel):
    # Uso de Optional para evitar repetir el código de VehiculoBase aquí
    registro_nro: Optional[int] = None
    registro_marca: Optional[bool] = None   
    fecha_titulo: Optional[date] = None
    marca_id: Optional[int] = None
    modelo_id: Optional[int] = None
    tipo_vehiculo_id: Optional[int] = None
    carroceria_id: Optional[int] = None
    anio: Optional[int] = None
    plazas: Optional[int] = None
    carga: Optional[int] = None
    tipo_motor_id: Optional[int] = None
    ejes: Optional[int] = None
    condicion_id: Optional[int] = None
    motor_marca: Optional[str] = None
    motor_nro: Optional[str] = None
    dominio: Optional[str] = None
    dominio_anterior: Optional[str] = None
    chasis_marca: Optional[str] = None
    chasis_nro: Optional[str] = None
    tipo_dominio: Optional[str] = None
    situacion_id: Optional[int] = None
    tipo_aptitud_id: Optional[int] = None
    tipo_cabina_id : Optional[int] = None
    tipo_traccion_id: Optional[int] = None
    fechaVtv: Optional[date] = None
    observaciones: Optional[str] = None
    update_user: Optional[str] = None
    dependencia_id: Optional[int] = None
    empresa: Optional[str] = None
    ri_anterior: Optional[int] = None
class Vehiculo(VehiculoBase):
    id: int
    dominio: Optional[str] = None
    created_at: datetime 
    updated_at: datetime 

    # Relaciones base...
    dependencia: Optional[VehiculoDependenciaBase] = None
    tipo_marca: Optional[TipoMarcaBase] = None
    tipo_modelo: Optional[TipoModeloBase] = None
    tipo_vehiculo: Optional[TipoVehiculoBase] = None
    tipo_carroceria: Optional[TipoCarroceria] = None
    tipo_motor: Optional[TipoMotorBase] = None
    tipo_condicion: Optional[TipoCondicionBase] = None
    tipo_situacion: Optional[TipoSituacionBase] = None
    tipo_aptitud: Optional[TipoAptitudBase] = None
    tipo_cabina: Optional[TipoCabinaBase] = None
    tipo_traccion: Optional[TipoTraccionBase] = None
    
    # Referencia en string, la clase 'Vtv' se resolverá con model_rebuild()
    # vtvs: List["Vtv"] = Field(default_factory=list)
    # novedades: List["Novedad"] = Field(default_factory=list)

class Vehiculo_by_Anio(BaseModel):
    descripcion: Optional[str]
    value: int

class Vehiculo_by_Dependencia(BaseModel):
    descripcion: Optional[str]
    value: int
class Vehiculo_by_Condicion(BaseModel):
    descripcion: Optional[str]
    value: int   

    model_config = ConfigDict(from_attributes=True)

class VehiculoPaginated(BaseModel):
    total: int
    data: List[Vehiculo]
class HistorialDependenciaSchema(BaseModel):
    id: Optional[str] = None
    registro_nro: Optional[int] = None
    dominio: Optional[str] = None
    activo: bool
    fecha_desde: Optional[date] = None
    fecha_hasta: Optional[date] = None
    dependencia: Optional[str] = None
    tipo_tramite: Optional[str] = None

    class Config:
        from_attributes = True
    
# ⚠️ No se necesita model_rebuild() aquí.