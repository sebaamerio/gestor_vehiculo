from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_vtvResultado_repository
from ..schemas.tipo_vtvResultado_schema import TipoVtvResultadoCreate


def get_all(db: Session): 
    return tipo_vtvResultado_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_vtvResultado_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de vtvResultado con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_vtvResultado: TipoVtvResultadoCreate):
    existing = tipo_vtvResultado_repository.get_by_descripcion(db, tipo_vtvResultado.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de vtvResultado '{tipo_vtvResultado.descripcion}' ya existe"
        )
    return tipo_vtvResultado_repository.create(db, tipo_vtvResultado)


def update(db: Session, id: int, tipo_vtvResultado: TipoVtvResultadoCreate):   
    db_tipo = tipo_vtvResultado_repository.update(db, id, tipo_vtvResultado)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de vtvResultado con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_vtvResultado_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de vtvResultado con id={id} no encontrado"
        )
    return {"message": f"Tipo de vtvResultado con id={id} eliminado correctamente"}