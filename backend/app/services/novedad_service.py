from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import novedad_repository
from ..schemas.novedad_schema import (
    Novedad,
    NovedadCreate, 
    NovedadUpdate, 
    DetalleWrapper, 
    NovedadResponse,
    DetalleBajaResponse, # <-- Importado
    DetalleCambioMotorResponse, # <-- Importar todos los tipos de respuesta necesarios
    DetalleAccidenteResponse, 
    DetalleDonacionResponse,
    DetalleTransfMunicipalidadResponse,
    DetalleRoboResponse,
    DetalleTransferenciaResponse,
    DetalleCambioChasisResponse,
    DetalleComodatoResponse,
    DetalleInfraccionResponse
)
from ..schemas.baja_schema import Baja # <-- Importado para mapear el detalle
from ..schemas.cambio_motor_schema import CambioMotor
from ..schemas.cambio_chasis_schema import CambioChasis
from ..schemas.accidente_schema import Accidente
from ..schemas.donacion_schema import Donacion
from ..schemas.robo_schema import Robo
from ..schemas.transferencia_schema import Transferencia
from ..schemas.comodato_schema import Comodato
from ..schemas.infraccion_schema import Infraccion

def get_all(db: Session):
    return novedad_repository.get_all(db)

def get_by_id(db: Session, id: int):
    item = novedad_repository.get_by_id(db, id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return item

def get_by_tipo(db: Session):
    return novedad_repository.get_by_tipo(db)

def get_by_vehiculoId(db: Session, vehiculo_id: int):
    item = novedad_repository.get_by_vehiculoId(db, vehiculo_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedades para el vehiculo={vehiculo_id} no encontrado"
        )
    return item

def create(db: Session, novedad: NovedadCreate, detalle: DetalleWrapper):

    # Llama al repositorio (devuelve NovedadORM y DetalleORM)
    db_novedad, db_detalle_orm = novedad_repository.create(
        db,
        novedad=novedad,
        detalle={
            "tipo": detalle.tipo,
            "data": detalle.data
        }
    )

    # =============================
    # 1) MAPA DE TIPOS A RESPUESTAS
    # =============================

    response_map = {
        "baja": (Baja, DetalleBajaResponse),
        "cambio_motor": (CambioMotor, DetalleCambioMotorResponse),
        "accidente": (Accidente, DetalleAccidenteResponse),
        "donacion": (Donacion, DetalleDonacionResponse),
        "transf_municipalidad": (Donacion, DetalleTransfMunicipalidadResponse),        
        "robo": (Robo, DetalleRoboResponse),
        "transferencia": (Transferencia, DetalleTransferenciaResponse),
        "cambio_chasis": (CambioChasis, DetalleCambioChasisResponse),
        "comodato": (Comodato, DetalleComodatoResponse),
        "infraccion": (Infraccion, DetalleInfraccionResponse)
    }

    if detalle.tipo not in response_map:
        raise ValueError(f"Tipo de detalle no soportado: {detalle.tipo}")

    ModeloPydantic, WrapperResponse = response_map[detalle.tipo]

    # =============================
    # 2) Construir el detalle
    # =============================

    detalle_pydantic = ModeloPydantic.model_validate(
        db_detalle_orm, from_attributes=True
    )

    detalle_response_wrapper = WrapperResponse(
        tipo=detalle.tipo,
        data=detalle_pydantic
    )

    # =============================
    # 3) Construir la novedad base
    # =============================

    novedad_pydantic = Novedad.model_validate(
        db_novedad, from_attributes=True
    ).model_dump()

    # Agregar el detalle
    novedad_pydantic["detalle"] = detalle_response_wrapper

    # =============================
    # 4) Respuesta final
    # =============================

    return NovedadResponse.model_validate(novedad_pydantic)

def update(db: Session, id: int, novedad: NovedadUpdate):
    db_tipo = novedad_repository.update(db, id, novedad)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La Novedad con id={id} no encontrado"
        )
    return db_tipo

def delete(db: Session, id: int):
    deleted = novedad_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La Novedad con id={id} no encontrado"
        )
    return {"message": f"La Novedad con id={id} eliminado correctamente"}