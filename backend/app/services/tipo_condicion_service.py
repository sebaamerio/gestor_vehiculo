from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_condicion_repository
from ..schemas.tipo_condicion_schema import TipoCondicionCreate


def get_all(db: Session): 
    return tipo_condicion_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_condicion_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de condicion con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_condicion: TipoCondicionCreate):
    existing = tipo_condicion_repository.get_by_descripcion(db, tipo_condicion.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de condicion '{tipo_condicion.descripcion}' ya existe"
        )
    return tipo_condicion_repository.create(db, tipo_condicion)


def update(db: Session, id: int, tipo_condicion: TipoCondicionCreate):   
    db_tipo = tipo_condicion_repository.update(db, id, tipo_condicion)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de condicion con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_condicion_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de condicion con id={id} no encontrado"
        )
    return {"message": f"Tipo de condicion con id={id} eliminado correctamente"}
