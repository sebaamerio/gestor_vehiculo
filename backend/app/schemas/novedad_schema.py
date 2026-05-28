from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from datetime import date, datetime
from typing import Optional, Literal, Union, Annotated

# Esquemas base de otras entidades (Asume que existen)
from .vehiculo_schema import VehiculoBase
from .tipo_novedad_schema import TipoNovedadBase

# Esquemas de detalle (CREATE/RESPONSE)
from .baja_schema import BajaCreate, Baja
from .cambio_motor_schema import CambioMotorCreate, CambioMotor
from .cambio_chasis_schema import CambioChasisCreate, CambioChasis
from .accidente_schema import AccidenteCreate, Accidente
from .donacion_schema import DonacionCreate, Donacion
from .robo_schema import RoboCreate, Robo
from .transferencia_schema import TransferenciaCreate, Transferencia
from .comodato_schema import ComodatoCreate, Comodato
from .infraccion_schema import InfraccionCreate, Infraccion

# =========================================
#             MODELOS BASE
# =========================================

class NovedadBase(BaseModel):
    vehiculo_id: int
    fecha: date
    tipo_novedad_id: int
    observaciones: Optional[str] = None
class NovedadCreate(NovedadBase):
    pass
class NovedadUpdate(BaseModel):
    fecha: Optional[date] = None
    observaciones: Optional[str] = None
    tipo_novedad_id: Optional[int] = None

# =========================================
#             RESPONSE MODEL (Base)
# =========================================
class Novedad(NovedadBase):
    id: int
    created_at: datetime
    updated_at: datetime

    tipo_novedad: Optional[TipoNovedadBase] = None
    vehiculo: Optional[VehiculoBase] = None

    model_config = ConfigDict(from_attributes=True)


# =========================================
#         MODELOS DETALLE (INPUT)
# =========================================
class DetalleBaja(BaseModel):
    tipo: Literal["baja"]
    data: BajaCreate
class DetalleCambioMotor(BaseModel):
    tipo: Literal["cambio_motor"]
    data: CambioMotorCreate
class DetalleCambioChasis(BaseModel):
    tipo: Literal["cambio_chasis"]
    data: CambioChasisCreate
class DetalleAccidente(BaseModel):
    tipo: Literal["accidente"]
    data: AccidenteCreate
class DetalleDonacion(BaseModel):
    tipo: Literal["donacion"]
    data: DonacionCreate
class DetalleTransfMunicipalidad(BaseModel):
    tipo: Literal["transf_municipalidad"]
    data: DonacionCreate
class DetalleRobo(BaseModel):
    tipo: Literal["robo"]
    data: RoboCreate
class DetalleTransferencia(BaseModel):
    tipo: Literal["transferencia"]
    data: TransferenciaCreate
class DetalleComodato(BaseModel):
    tipo: Literal["comodato"]
    data: ComodatoCreate
class DetalleInfraccion(BaseModel):
    tipo: Literal["infraccion"]
    data: InfraccionCreate

DetalleWrapper = Annotated[
    Union[
        DetalleBaja,
        DetalleCambioMotor,
        DetalleCambioChasis,
        DetalleAccidente,
        DetalleDonacion,
        DetalleTransfMunicipalidad,
        DetalleRobo,
        DetalleTransferencia,
        DetalleComodato,
        DetalleInfraccion
    ],
    Field(discriminator="tipo")
]

class NovedadPayload(BaseModel):
    novedad: NovedadCreate
    detalle: DetalleWrapper


# =========================================
#         MODELOS DETALLE (RESPONSE)
# =========================================
class DetalleBajaResponse(BaseModel):
    tipo: Literal["baja"]
    data: Baja
    model_config = ConfigDict(from_attributes=True)
class DetalleCambioMotorResponse(BaseModel):
    tipo: Literal["cambio_motor"]
    data: CambioMotor
    model_config = ConfigDict(from_attributes=True)
class DetalleCambioChasisResponse(BaseModel):
    tipo: Literal["cambio_chasis"]
    data: CambioChasis
    model_config = ConfigDict(from_attributes=True)
class DetalleAccidenteResponse(BaseModel):
    tipo: Literal["accidente"]
    data: Accidente
    model_config = ConfigDict(from_attributes=True)
class DetalleDonacionResponse(BaseModel):
    tipo: Literal["donacion"]
    data: Donacion
    model_config = ConfigDict(from_attributes=True)
class DetalleTransfMunicipalidadResponse(BaseModel):
    tipo: Literal["transf_municipalidad"]
    data: Donacion
    model_config = ConfigDict(from_attributes=True)
class DetalleRoboResponse(BaseModel):
    tipo: Literal["robo"]
    data: Robo
    model_config = ConfigDict(from_attributes=True)
class DetalleTransferenciaResponse(BaseModel):
    tipo: Literal["transferencia"]
    data: Transferencia
    model_config = ConfigDict(from_attributes=True)
class DetalleComodatoResponse(BaseModel):
    tipo: Literal["comodato"]
    data: Comodato
    model_config = ConfigDict(from_attributes=True)
class DetalleInfraccionResponse(BaseModel):
    tipo: Literal["infraccion"]
    data: Infraccion
    model_config = ConfigDict(from_attributes=True)


DetalleResponseWrapper = Annotated[
    Union[
        DetalleBajaResponse,
        DetalleCambioMotorResponse,
        DetalleCambioChasisResponse,
        DetalleAccidenteResponse,
        DetalleDonacionResponse,
        DetalleTransfMunicipalidadResponse,
        DetalleRoboResponse,
        DetalleTransferenciaResponse,
        DetalleComodatoResponse,
        DetalleInfraccionResponse
    ],
    Field(discriminator="tipo")
]


# =========================================
#         MODELO DE RESPUESTA FINAL
# =========================================
class NovedadResponse(Novedad):
    detalle: DetalleResponseWrapper # <--- Campo requerido en la respuesta
    model_config = ConfigDict(from_attributes=True)