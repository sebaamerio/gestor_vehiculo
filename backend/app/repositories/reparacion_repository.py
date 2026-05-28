from sqlalchemy.orm import Session
from ..models.reparacion_model import Reparacion
from ..schemas.reparacion_schema import ReparacionCreate, ReparacionUpdate

def get_all(db: Session):
    return db.query(Reparacion).all()

def get_by_id(db: Session, id: int):
    return db.query(Reparacion).filter(Reparacion.id == id).first()

def create(db: Session, data: ReparacionCreate):
    db_data = Reparacion(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def update(db: Session, id: int, data: ReparacionUpdate):
    db_data = get_by_id(db, id)
    if not db_data:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_data, field, value)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete(db: Session, id: int):
    db_data = get_by_id(db, id)
    if db_data:
        db.delete(db_data)
        db.commit()
    return db_data