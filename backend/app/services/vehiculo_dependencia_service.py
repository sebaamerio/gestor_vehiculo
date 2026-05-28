from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import vehiculo_dependencia_repository
from ..schemas.vehiculo_dependencia_schema import VehiculoDependenciaCreate, VehiculoDependenciaUpdate

def get_all(db: Session): 
    return vehiculo_dependencia_repository.get_all(db)


def get_by_id(db: Session, id: int):
    item = vehiculo_dependencia_repository.get_by_id(db, id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dependnecia con id={id} no encontrado"
        )
    return item


def create(db: Session, vehiculoDependencia: VehiculoDependenciaCreate):
    return vehiculo_dependencia_repository.create(db, vehiculoDependencia)


def update(db: Session, id: int, vehiculoDependencia: VehiculoDependenciaUpdate):   
    db_tipo = vehiculo_dependencia_repository.update(db, id, vehiculoDependencia)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dependencia con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = vehiculo_dependencia_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dependencia con id={id} no encontrado"
        )
    return {"message": f"Dependencia con id={id} eliminado correctamente"}