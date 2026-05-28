from pydantic import BaseModel
class TipoAptitudBase(BaseModel):  
    descripcion: str
class TipoAptitudCreate(TipoAptitudBase):
    pass
class TipoAptitud(TipoAptitudBase):
    id: int

    model_config = {
        "from_attributes": True
    }
