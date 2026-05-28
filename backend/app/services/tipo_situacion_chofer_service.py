from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_situacion_chofer_repository
from ..schemas.tipo_situacion_chofer_schema import TipoSituacionChoferCreate


def get_all(db: Session): 
    return tipo_situacion_chofer_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_situacion_chofer_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de situacion con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_situacion: TipoSituacionChoferCreate):
    existing = tipo_situacion_chofer_repository.get_by_descripcion(db, tipo_situacion.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de situacion '{tipo_situacion.descripcion}' ya existe"
        )
    return tipo_situacion_chofer_repository.create(db, tipo_situacion)


def update(db: Session, id: int, tipo_situacion: TipoSituacionChoferCreate):   
    db_tipo = tipo_situacion_chofer_repository.update(db, id, tipo_situacion)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de situacion con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_situacion_chofer_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de situacion con id={id} no encontrado"
        )
    return {"message": f"Tipo de situacion con id={id} eliminado correctamente"}