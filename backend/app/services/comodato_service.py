from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import comodato_repository
from ..schemas.comodato_schema import ComodatoUpdate

def get_all(db: Session): 
    return comodato_repository.get_all(db)

def get_by_id(db: Session, id: int):
    tipo = comodato_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return tipo

def get_by_NovedadId(db: Session, novedad_id: int):
    item = comodato_repository.get_by_novedad_id(db, novedad_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return item

def update(db: Session, id: int, data: ComodatoUpdate):
    db_donacion = comodato_repository.update(db, id, data)
    if not db_donacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return db_donacion
