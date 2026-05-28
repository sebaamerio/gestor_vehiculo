from sqlalchemy.orm import Session
from ..repositories import localidad_repository
from ..schemas.localidad_schema import LocalidadCreate

def get_all(db: Session):
    return localidad_repository.get_all(db)

def get_by_id(db: Session, id: int):
    return localidad_repository.get_by_id(db, id)

def create(db: Session, localidad: LocalidadCreate):
    return localidad_repository.create(db, localidad)

def delete(db: Session, id: int):
    return localidad_repository.delete(db, id)
