from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_modelo_repository
from ..schemas.tipo_modelo_schema import TipoModeloCreate


def get_all(db: Session): 
    return tipo_modelo_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_modelo_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de modelo con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_modelo: TipoModeloCreate):
    existing = tipo_modelo_repository.get_by_descripcion(db, tipo_modelo.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de modelo '{tipo_modelo.descripcion}' ya existe"
        )
    return tipo_modelo_repository.create(db, tipo_modelo)


def update(db: Session, id: int, tipo_modelo: TipoModeloCreate):
    db_tipo = tipo_modelo_repository.update(db, id, tipo_modelo)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de modelo con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_modelo_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de modelo con id={id} no encontrado"
        )
    return {"message": f"Tipo de modelo con id={id} eliminado correctamente"}
