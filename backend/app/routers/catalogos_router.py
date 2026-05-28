from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user
from ..schemas.catalogo_schema import Catalogo

from ..services import (
  tipo_vehiculo_service,
  tipo_acto_service,
  tipo_carroceria_service,
  tipo_condicion_service,
  tipo_motor_service,
  tipo_novedad_service,
  tipo_situacion_service,
  tipo_vtvResultado_service,
  tipo_marca_service,
  tipo_documento_service,
  dependencia_service,
  tipo_situacion_chofer_service,
  tipo_pago_service
)

router = APIRouter(prefix="/catalogos", tags=["Catalogo"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=Catalogo)
def get_catalogos(db: Session = Depends(get_db)):
    return {       
        "tipoVehiculos": tipo_vehiculo_service.get_all(db),
        "tipoActos": tipo_acto_service.get_all(db),
        "tipoCarrocerias": tipo_carroceria_service.get_all(db),
        "tipoCondiciones": tipo_condicion_service.get_all(db),
        "tipoMotores": tipo_motor_service.get_all(db),
        "tipoNovedades": tipo_novedad_service.get_all(db),
        "tipoSituaciones": tipo_situacion_service.get_all(db),
        "tipoVtvResultados": tipo_vtvResultado_service.get_all(db),
        "tipoMarca": tipo_marca_service.get_all(db),
        "dependencia" : dependencia_service.get_all(db),
        "tipoDocumento" : tipo_documento_service.get_all(db),
        "tipoSituacionesChofer": tipo_situacion_chofer_service.get_all(db),
        "tipoPago": tipo_pago_service.get_all(db)
    }
