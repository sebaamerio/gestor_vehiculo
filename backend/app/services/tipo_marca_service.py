from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_marca_repository
from ..schemas.tipo_marca_schema import TipoMarcaCreate


def get_all(db: Session): 
    return tipo_marca_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_marca_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de marca con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_marca: TipoMarcaCreate):
    existing = tipo_marca_repository.get_by_descripcion(db, tipo_marca.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de marca '{tipo_marca.descripcion}' ya existe"
        )
    return tipo_marca_repository.create(db, tipo_marca)


def update(db: Session, id: int, tipo_marca: TipoMarcaCreate):
    db_tipo = tipo_marca_repository.update(db, id, tipo_marca)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de marca con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_marca_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de marca con id={id} no encontrado"
        )
    return {"message": f"Tipo de marca con id={id} eliminado correctamente"}