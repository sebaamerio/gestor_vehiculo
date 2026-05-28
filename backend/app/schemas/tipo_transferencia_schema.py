from pydantic import BaseModel

# ======================
# Base
# ======================
class TipoTramiteDependenciaBase(BaseModel):
    descripcion: str

# ======================
# Create
# ====================== 
class TipoTramiteDependenciaCreate(TipoTramiteDependenciaBase):
    pass

class TipoTramiteDependencia(TipoTramiteDependenciaBase):
    id: int

    model_config = {
        "from_attributes": True
    }