from pydantic import BaseModel
class TipoActoBase(BaseModel):  
    descripcion: str
class TipoActoCreate(TipoActoBase):
    pass
class TipoActo(TipoActoBase):
    id: int

    model_config = {
        "from_attributes": True
    }
