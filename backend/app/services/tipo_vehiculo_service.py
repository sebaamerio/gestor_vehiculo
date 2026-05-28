from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_vehiculo_repository
from ..schemas.tipo_vehiculo_schema import TipoVehiculoCreate


def get_all(db: Session): 
    return tipo_vehiculo_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_vehiculo_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de vehículo con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_vehiculo: TipoVehiculoCreate):
    existing = tipo_vehiculo_repository.get_by_descripcion(db, tipo_vehiculo.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de vehículo '{tipo_vehiculo.descripcion}' ya existe"
        )
    return tipo_vehiculo_repository.create(db, tipo_vehiculo)


def update(db: Session, id: int, tipo_vehiculo: TipoVehiculoCreate):
    db_tipo = tipo_vehiculo_repository.update(db, id, tipo_vehiculo)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de vehículo con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_vehiculo_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de vehículo con id={id} no encontrado"
        )
    return {"message": f"Tipo de vehículo con id={id} eliminado correctamente"}
