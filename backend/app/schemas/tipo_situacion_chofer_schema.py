from pydantic import BaseModel

class TipoSituacionChoferBase(BaseModel):  
    descripcion: str

class TipoSituacionChoferCreate(TipoSituacionChoferBase):
    pass

class TipoSituacionChofer(TipoSituacionChoferBase):
    id: int

    model_config = {
        "from_attributes": True
    }