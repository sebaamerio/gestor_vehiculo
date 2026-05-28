from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


# ======================
# Base
# ======================
class VehiculoDependenciaBase(BaseModel):
    fecha_desde: date
    fecha_hasta: Optional[date] = None
    expediente: Optional[str] = Field(None, max_length=50)
    acto_id: Optional[int] = None
    norma: Optional[str] = Field(None, max_length=50)
    dependencia_descripcion: Optional[str] = Field(None, max_length=100)
    activo: bool = True
    observaciones: Optional[str] = Field(None, max_length=150)
    vehiculo_id: int
    dependencia_id: Optional[int] = None
    tipo_tramite_id: Optional[int] = None
    update_user: Optional[str] = Field(None, max_length=60)


# ======================
# Create
# ======================
class VehiculoDependenciaCreate(VehiculoDependenciaBase):
    pass


# ======================
# Update (parcial)
# ======================
class VehiculoDependenciaUpdate(BaseModel):
    fecha_desde: Optional[date] = None
    fecha_hasta: Optional[date] = None
    expediente: Optional[str] = Field(None, max_length=50)
    acto_id: Optional[int] = None
    norma: Optional[str] = Field(None, max_length=50)
    dependencia_descripcion: Optional[str] = Field(None, max_length=100)
    activo: Optional[bool] = None
    observaciones: Optional[str] = Field(None, max_length=150)
    dependencia_id: Optional[int] = None
    update_user: Optional[str] = Field(None, max_length=60)


# ======================
# Read / Response
# ======================
class VehiculoDependencia(VehiculoDependenciaBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }