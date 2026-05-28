from sqlalchemy.orm import Session
from ..models.provincia_model import Provincia
from ..schemas.provincia_schema import ProvinciaCreate

def get_all(db: Session):
    return db.query(Provincia).all()

def get_by_id(db: Session, id: int):
    return db.query(Provincia).filter(Provincia.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca una provincia por su descripción (case insensitive)."""
    return db.query(Provincia).filter(
        Provincia.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, provincia: ProvinciaCreate):
    nueva_provincia = Provincia(**provincia.model_dump())
    db.add(nueva_provincia)
    db.commit()
    db.refresh(nueva_provincia)
    return nueva_provincia

def delete(db: Session, id: int):
    db_provincia = get_by_id(db, id)
    if db_provincia:
        db.delete(db_provincia)
        db.commit()
    return db_provincia
