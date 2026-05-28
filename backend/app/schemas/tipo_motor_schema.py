from pydantic import BaseModel

class TipoMotorBase(BaseModel):  
    descripcion: str

class TipoMotorCreate(TipoMotorBase):
    pass

class TipoMotor(TipoMotorBase):
    id: int

    model_config = {
        "from_attributes": True
    }
