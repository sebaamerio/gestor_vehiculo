from pydantic import BaseModel

class TipoCarroceriaBase(BaseModel): 
    descripcion: str
class TipoCarroceriaCreate(TipoCarroceriaBase):
    pass
class TipoCarroceria(TipoCarroceriaBase):
    id: int

    model_config = {
        "from_attributes": True
    }
