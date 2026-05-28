from pydantic import BaseModel

class TipoSituacionBase(BaseModel):  
    descripcion: str

class TipoSituacionCreate(TipoSituacionBase):
    pass

class TipoSituacion(TipoSituacionBase):
    id: int

    model_config = {
        "from_attributes": True
    }