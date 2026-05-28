from pydantic import BaseModel
from ..schemas.tipo_modelo_schema import TipoModelo
from typing import List, TYPE_CHECKING

# Evitamos ciclos de importación
if TYPE_CHECKING:
    from ..schemas.tipo_modelo_schema import TipoModelo
class TipoMarcaBase(BaseModel):  
    descripcion: str
class TipoMarcaCreate(TipoMarcaBase):
    pass

class TipoMarcaSinModelo(TipoMarcaBase):
    id: int  
class TipoMarca(TipoMarcaBase):
    id: int
    modelos: List["TipoModelo"] = []  # referencia diferida

    model_config = {"from_attributes": True}

# 🔧 Reconstruir relaciones
TipoMarca.model_rebuild()
TipoModelo.model_rebuild()