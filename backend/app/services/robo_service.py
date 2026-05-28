from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import robo_repository
from ..schemas.robo_schema import RoboUpdate

def get_all(db: Session): 
    return robo_repository.get_all(db)

def get_by_id(db: Session, id: int):
    tipo = robo_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return tipo

def get_by_NovedadId(db: Session, novedad_id: int):
    item = robo_repository.get_by_novedad_id(db, novedad_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return item

def update(db: Session, id: int, robo: RoboUpdate):
    db_robo = robo_repository.update(db, id, robo)
    if not db_robo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return db_robo