from pydantic import BaseModel

class TipoDocumentoBase(BaseModel):
    descripcion: str

class TipoDocumentoCreate(TipoDocumentoBase):
    pass

class TipoDocumento(TipoDocumentoBase):
    id: int

    model_config = {
        "from_attributes": True
    }
