from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import taller_repository
from ..schemas.taller_schema import TallerCreate, TallerUpdate


def get_all(db: Session): 
    return taller_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = taller_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Taller con id={id} no encontrado"
        )
    return tipo


def create(db: Session, taller: TallerCreate):
    existing = taller_repository.get_by_descripcion(db, taller.taller_desc)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Taller '{taller.taller_desc}' ya existe"
        )
    return taller_repository.create(db, taller)


def update(db: Session, id: int, taller: TallerUpdate):   
    db_tipo = taller_repository.update(db, id, taller)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Taller con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = taller_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Taller con id={id} no encontrado"
        )
    return {"message": f"Taller con id={id} eliminado correctamente"}