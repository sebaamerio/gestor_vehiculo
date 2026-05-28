from pydantic import BaseModel

class TipoPagoBase(BaseModel):  
    descripcion: str

class TipoPagoCreate(TipoPagoBase):
    pass

class TipoPago(TipoPagoBase):
    id: int

    model_config = {
        "from_attributes": True
    }
