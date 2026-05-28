from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_acto_repository
from ..schemas.tipo_acto_schema import TipoActoCreate


def get_all(db: Session): 
    return tipo_acto_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_acto_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de acto con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_acto: TipoActoCreate):
    existing = tipo_acto_repository.get_by_descripcion(db, tipo_acto.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de acto '{tipo_acto.descripcion}' ya existe"
        )
    return tipo_acto_repository.create(db, tipo_acto)


def update(db: Session, id: int, tipo_acto: TipoActoCreate):   
    db_tipo = tipo_acto_repository.update(db, id, tipo_acto)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de acto con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_acto_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de acto con id={id} no encontrado"
        )
    return {"message": f"Tipo de acto con id={id} eliminado correctamente"}
