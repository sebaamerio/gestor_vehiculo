from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import baja_repository
from ..schemas.baja_schema import BajaUpdate

def get_all(db: Session): 
    return baja_repository.get_all(db)

def get_by_id(db: Session, id: int):
    tipo = baja_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return tipo

def get_by_NovedadId(db: Session, novedad_id: int):
    item = baja_repository.get_by_novedad_id(db, novedad_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return item

def update(db: Session, id: int, baja: BajaUpdate):
    db_baja = baja_repository.update(db, id, baja)
    if not db_baja:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    if baja.fecha or baja.observaciones:
        db_novedad = db_baja.novedad
        if db_novedad:
            if baja.fecha:
                db_novedad.fecha = baja.fecha
            if baja.observaciones:
                db_novedad.observaciones = baja.observaciones
            db.commit()
            db.refresh(db_baja)
    return db_baja
