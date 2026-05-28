from pydantic import BaseModel
from typing import List, TYPE_CHECKING

# ✅ Evita importar directamente para prevenir ciclo
if TYPE_CHECKING:
    from ..schemas.localidad_schema import Localidad

class ProvinciaBase(BaseModel):  
    descripcion: str

class ProvinciaCreate(ProvinciaBase):
    pass

class Provincia(ProvinciaBase):
    id: int
    # 👇 usamos string "Localidad" para referencia diferida
    localidades: List["Localidad"] = []

    class Config:
        from_attributes = True