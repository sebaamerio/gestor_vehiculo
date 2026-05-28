from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import accidente_repository
from ..schemas.accidente_schema import AccidenteUpdate

def get_all(db: Session): 
    return accidente_repository.get_all(db)

def get_by_id(db: Session, id: int):
    tipo = accidente_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return tipo

def get_by_NovedadId(db: Session, novedad_id: int):
    item = accidente_repository.get_by_novedad_id(db, novedad_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return item

def update(db: Session, id: int, accidente: AccidenteUpdate):
    db_accidente = accidente_repository.update(db, id, accidente)
    if not db_accidente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    if accidente.fecha or accidente.observaciones:
        db_novedad = db_accidente.novedad
        if db_novedad:
            if accidente.fecha:
                db_novedad.fecha = accidente.fecha
            if accidente.observaciones:
                db_novedad.observaciones = accidente.observaciones
            db.commit()
            db.refresh(db_accidente)
    return db_accidente
