from pydantic import BaseModel
class TipoCabinaBase(BaseModel):  
    descripcion: str
class TipoCabinaCreate(TipoCabinaBase):
    pass
class TipoCabina(TipoCabinaBase):
    id: int

    model_config = {
        "from_attributes": True
    }
