from pydantic import BaseModel
from typing import Optional
class DependenciaBase(BaseModel):   
    descripcion: str
class DependenciaCreate(DependenciaBase):
    pass
class DependenciaUpdate(DependenciaBase):
    descripcion: Optional[str] = None
class Dependencia(DependenciaBase):
    id: int

    model_config = {
        "from_attributes": True
    }