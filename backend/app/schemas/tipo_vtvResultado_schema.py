from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from typing import List, Optional, TYPE_CHECKING

# Usamos TYPE_CHECKING aquí ya que TipoVtvResultado no causa el ciclo principal.
if TYPE_CHECKING:
    from .vtv_schema import Vtv 

class TipoVtvResultadoBase(BaseModel):
    descripcion: str

class TipoVtvResultadoCreate(TipoVtvResultadoBase):
    pass

class TipoVtvResultadoSinVtv(TipoVtvResultadoBase):
    """
    Esquema utilizado para evitar la recursión infinita o anidación excesiva 
    al ser referenciado por un Vtv.
    """
    id: int

class TipoVtvResultado(TipoVtvResultadoBase):
    id: int
    
    # Referencia adelantada (en string)
    # vtvs: List["Vtv"] = [] 

    model_config = ConfigDict(from_attributes=True)
    
# ⚠️ No se necesita model_rebuild() aquí.