from pydantic import BaseModel
from typing import Optional, TYPE_CHECKING

class TallerBase(BaseModel):      
    taller_desc :str
    domicilio : Optional[str] = None
    cuit : Optional[str] = None
    ing_brutos : Optional[str] = None
    observaciones : Optional[str] = None

class TallerCreate(TallerBase):
    pass
   
class TallerUpdate(TallerBase):
    taller_desc :Optional[str] = None
    domicilio : Optional[str] = None
    cuit : Optional[str] = None
    ing_brutos : Optional[str] = None
    observaciones : Optional[str] = None

class Taller(TallerBase):
    id: int

    model_config = {
        "from_attributes": True
    }
