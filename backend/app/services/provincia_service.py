from sqlalchemy.orm import Session
from ..repositories import provincia_repository
from ..schemas.provincia_schema import ProvinciaCreate

def get_all(db: Session):
    return provincia_repository.get_all(db)

def get_by_id(db: Session, id: int):
    return provincia_repository.get_by_id(db, id)

def create(db: Session, provincia: ProvinciaCreate):
    return provincia_repository.create(db, provincia)

def delete(db: Session, id: int):
    return provincia_repository.delete(db, id)
