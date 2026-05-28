from pydantic import BaseModel

class TipoReparacionEstadoBase(BaseModel):
    descripcion: str

class TipoReparacionEstadoCreate(TipoReparacionEstadoBase):
    pass

class TipoReparacionEstadosinReparacion(TipoReparacionEstadoBase):
    """
    Esquema utilizado para evitar la recursión infinita o anidación excesiva 
    al ser referenciado por un Vtv.
    """
    id: int

class TipoReparacionEstado(TipoReparacionEstadoBase):
    id: int

    model_config = {
        "from_attributes": True
    }
