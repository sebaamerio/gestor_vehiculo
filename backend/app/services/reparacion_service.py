from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import reparacion_repository
from ..schemas.reparacion_schema import ReparacionCreate, ReparacionUpdate

def get_all(db: Session):
    return reparacion_repository.get_all(db)

def get_by_id(db: Session, id: int):
    item = reparacion_repository.get_by_id(db, id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Reparacion con id={id} no encontrado"
        )
    return item

def create(db: Session, vtv: ReparacionCreate):
    return reparacion_repository.create(db, vtv)

def update(db: Session, id: int, data: ReparacionUpdate):
    db_reparacion = reparacion_repository.update(db, id, data)
    if not db_reparacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Reparacion con id={id} no encontrado"
        )
    return db_reparacion

def delete(db: Session, id: int):
    deleted = reparacion_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Reparacion con id={id} no encontrado"
        )
    return {"message": f"Reparacion con id={id} eliminado correctamente"}
