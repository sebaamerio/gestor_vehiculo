from pydantic import BaseModel
from typing import List
from ..schemas.tipo_vehiculo_schema import TipoVehiculo
from ..schemas.tipo_acto_schema import TipoActo
from ..schemas.tipo_carroceria_schema import TipoCarroceria
from ..schemas.tipo_condicion_schema import TipoCondicion
from ..schemas.tipo_motor_schema import TipoMotor
from ..schemas.tipo_novedad_schema import TipoNovedad
from ..schemas.tipo_situacion_schema import TipoSituacion
from ..schemas.tipo_vtvResultado_schema import TipoVtvResultado
from ..schemas.dependencia_schema import Dependencia
from ..schemas.tipo_marca_schema import TipoMarcaSinModelo
from ..schemas.tipo_documento_schema import TipoDocumento
from ..schemas.tipo_situacion_chofer_schema import TipoSituacionChofer
from ..schemas.tipo_pago_schema import TipoPago


class Catalogo(BaseModel):
    tipoVehiculos: List[TipoVehiculo]
    tipoActos: List[TipoActo]
    tipoCarrocerias: List[TipoCarroceria]
    tipoCondiciones: List[TipoCondicion]
    tipoMotores: List[TipoMotor]
    tipoNovedades: List[TipoNovedad]
    tipoSituaciones: List[TipoSituacion]
    tipoVtvResultados: List[TipoVtvResultado]
    tipoMarca: List[TipoMarcaSinModelo]
    tipoDocumento: List[TipoDocumento]
    dependencia: List[Dependencia]
    tipoSituacionesChofer: List[TipoSituacionChofer]
    tipoPago: List[TipoPago]
    class Config:
        from_attributes = True  # permite usar objetos ORM
