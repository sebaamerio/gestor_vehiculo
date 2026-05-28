from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_aptitud_repository
from ..schemas.tipo_aptitud_schema import TipoAptitudCreate


def get_all(db: Session): 
    return tipo_aptitud_repository.get_all(db)

def get_by_id(db: Session, id: int):
    tipo = tipo_aptitud_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo con id={id} no encontrado"
        )
    return tipo

def create(db: Session, tipo: TipoAptitudCreate):
    existing = tipo_aptitud_repository.get_by_descripcion(db, tipo.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo '{tipo.descripcion}' ya existe"
        )
    return tipo_aptitud_repository.create(db, tipo)

def update(db: Session, id: int, tipo: TipoAptitudCreate):   
    db_tipo = tipo_aptitud_repository.update(db, id, tipo)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo con id={id} no encontrado"
        )
    return db_tipo

def delete(db: Session, id: int):
    deleted = tipo_aptitud_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo con id={id} no encontrado"
        )
    return {"message": f"Tipo con id={id} eliminado correctamente"}