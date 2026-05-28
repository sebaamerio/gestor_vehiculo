from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..schemas.tipo_marca_schema import TipoMarcaBase

class TipoModeloBase(BaseModel): 
    descripcion: str
    marca_id: int

class TipoModeloCreate(TipoModeloBase):
    pass

class TipoModelo(TipoModeloBase):
    id: int   

    model_config = {"from_attributes": True}
