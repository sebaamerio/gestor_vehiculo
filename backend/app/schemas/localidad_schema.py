from pydantic import BaseModel
from typing import Optional
from ..schemas.provincia_schema import ProvinciaBase, Provincia

class LocalidadBase(BaseModel):   
    descripcion: str
    partido_id: str
    cod_postal: Optional[int] = 0
    provincia_id: int

class LocalidadCreate(LocalidadBase):
    pass

class LocalidadUpdate(BaseModel):
    descripcion: Optional[str] = None
    partido_id: Optional[str] = None
    cod_postal: Optional[int] = 0
    provincia_id: Optional[int] = None

class Localidad(LocalidadBase):
    id: int
    provincia: ProvinciaBase  # ✅ relación simplificada, sin importar todo Provincia

    class Config:
        from_attributes = True

Provincia.model_rebuild()