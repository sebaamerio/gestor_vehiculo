from pydantic import BaseModel
class TipoTraccionBase(BaseModel):  
    descripcion: str
class TipoTraccionCreate(TipoTraccionBase):
    pass
class TipoTraccion(TipoTraccionBase):
    id: int

    model_config = {
        "from_attributes": True
    }
