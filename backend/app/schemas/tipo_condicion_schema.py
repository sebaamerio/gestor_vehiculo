from pydantic import BaseModel
from typing import Optional
class TipoCondicionBase(BaseModel):   
    descripcion: str
    icon : Optional[str] = None
class TipoCondicionCreate(TipoCondicionBase):
    pass

class TipoCondicionUpdate(TipoCondicionBase):
    descripcion: Optional[str] = None
    icon: Optional[int] = None
class TipoCondicion(TipoCondicionBase):
    id: int

    model_config = {
        "from_attributes": True
    }
