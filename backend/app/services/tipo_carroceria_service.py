from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_carroceria_repository
from ..schemas.tipo_carroceria_schema import TipoCarroceriaCreate


def get_all(db: Session): 
    return tipo_carroceria_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_carroceria_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de carroceria con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_carroceria: TipoCarroceriaCreate):
    existing = tipo_carroceria_repository.get_by_descripcion(db, tipo_carroceria.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de carroceria '{tipo_carroceria.descripcion}' ya existe"
        )
    return tipo_carroceria_repository.create(db, tipo_carroceria)


def update(db: Session, id: int, tipo_carroceria: TipoCarroceriaCreate):   
    db_tipo = tipo_carroceria_repository.update(db, id, tipo_carroceria)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de carroceria con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_carroceria_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de carroceria con id={id} no encontrado"
        )
    return {"message": f"Tipo de carroceria con id={id} eliminado correctamente"}
