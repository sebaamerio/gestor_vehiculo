from pydantic import BaseModel
from datetime import date
from typing import Optional, TYPE_CHECKING
from typing import Optional, List

# para evitar ciclo 
if TYPE_CHECKING:
    from .tipo_documento_schema import TipoDocumento
    from .dependencia_schema import Dependencia
    from .localidad_schema import Localidad
    from .tipo_situacion_chofer_schema import TipoSituacionChofer   

class ChoferBase(BaseModel):
    tipo_documento_id: Optional[int] = None
    documento: Optional[str] = None
    nombre: str
    cargo: Optional[int] = None
    licencia: Optional[str] = None
    dependencia_id: Optional[int] = None
    domicilio: Optional[str] = None
    localidad_id: Optional[int] = None
    telefono: Optional[str] = None
    tipo_situacion_chofer_id: Optional[int] = None
    observacion: Optional[str] = None
    clase: Optional[int] = None
    fecha_nacimiento: Optional[date] = None
    licencia_vto: Optional[date] = None

class ChoferCreate(ChoferBase):
    pass

class ChoferUpdate(ChoferBase):
    tipo_documento_id: Optional[int] = None
    documento: Optional[str] = None
    nombre: Optional[str] = None
    cargo: Optional[int] = None
    licencia: Optional[str] = None
    dependencia_id: Optional[int] = None
    domicilio: Optional[str] = None
    localidad_id: Optional[int] = None
    telefono: Optional[str] = None
    tipo_situacion_chofer_id: Optional[int] = None
    observacion: Optional[str] = None
    clase: Optional[int] = None
    fecha_nacimiento: Optional[date] = None
    licencia_vto: Optional[date] = None


class Chofer(ChoferBase):
    id: int

    tipo_documento: Optional["TipoDocumento"] = None
    dependencia: Optional["Dependencia"] = None
    localidad: Optional["Localidad"] = None
    tipo_situacion_chofer: Optional["TipoSituacionChofer"] = None

    model_config = {
        "from_attributes": True
    }
class ChoferPaginated(BaseModel):
    total: int
    data: List[Chofer]

    model_config = {
        "from_attributes": True
    }
class ChoferesByLicencia(BaseModel):
    descripcion: str
    value: int

from .tipo_documento_schema import TipoDocumento
from .dependencia_schema import Dependencia
from .localidad_schema import Localidad
from .tipo_situacion_chofer_schema import TipoSituacionChofer 
Chofer.model_rebuild()