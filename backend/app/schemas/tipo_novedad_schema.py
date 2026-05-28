from pydantic import BaseModel

class TipoNovedadBase(BaseModel): 
    descripcion: str

class TipoNovedadCreate(TipoNovedadBase):
    pass

class TipoNovedad(TipoNovedadBase):
    id: int

    model_config = {
        "from_attributes": True
    }