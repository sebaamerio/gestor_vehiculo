from pydantic import BaseModel

class TipoVehiculoBase(BaseModel):   
    descripcion: str

class TipoVehiculoCreate(TipoVehiculoBase):
    pass

class TipoVehiculo(TipoVehiculoBase):
    id: int

    model_config = {
        "from_attributes": True
    }
