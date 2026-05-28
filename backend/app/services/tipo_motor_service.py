from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_motor_repository
from ..schemas.tipo_motor_schema import TipoMotorCreate


def get_all(db: Session): 
    return tipo_motor_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_motor_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de motor con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_motor: TipoMotorCreate):
    existing = tipo_motor_repository.get_by_descripcion(db, tipo_motor.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de motor '{tipo_motor.descripcion}' ya existe"
        )
    return tipo_motor_repository.create(db, tipo_motor)


def update(db: Session, id: int, tipo_motor: TipoMotorCreate):   
    db_tipo = tipo_motor_repository.update(db, id, tipo_motor)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de motor con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_motor_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de motor con id={id} no encontrado"
        )
    return {"message": f"Tipo de motor con id={id} eliminado correctamente"}
