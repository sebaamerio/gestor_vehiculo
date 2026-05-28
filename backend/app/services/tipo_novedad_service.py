from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_novedad_repository
from ..schemas.tipo_novedad_schema import TipoNovedadCreate


def get_all(db: Session): 
    return tipo_novedad_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_novedad_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de novedad con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_novedad: TipoNovedadCreate):
    existing = tipo_novedad_repository.get_by_descripcion(db, tipo_novedad.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de novedad '{tipo_novedad.descripcion}' ya existe"
        )
    return tipo_novedad_repository.create(db, tipo_novedad)


def update(db: Session, id: int, tipo_novedad: TipoNovedadCreate):   
    db_tipo = tipo_novedad_repository.update(db, id, tipo_novedad)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de novedad con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_novedad_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de novedad con id={id} no encontrado"
        )
    return {"message": f"Tipo de novedad con id={id} eliminado correctamente"}