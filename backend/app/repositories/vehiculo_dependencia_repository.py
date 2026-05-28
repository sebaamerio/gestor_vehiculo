from sqlalchemy.orm import Session
from sqlalchemy import func, asc, desc
from ..models.vehiculo_dependencia_model import VehiculoDependencia
from ..schemas.vehiculo_dependencia_schema import VehiculoDependenciaCreate, VehiculoDependenciaUpdate


def get_all(db: Session):
    return db.query(VehiculoDependencia).all()

def get_by_id(db: Session, id: int):
    return db.query(VehiculoDependencia).filter(VehiculoDependencia.id == id).first()


def create(db: Session, vehiculoDependencia: VehiculoDependenciaCreate):
    db_item = VehiculoDependencia(**vehiculoDependencia.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update(db: Session, id: int, vehiculoDependencia: VehiculoDependenciaUpdate):
    db_item = get_by_id(db, id)
    if not db_item:
        return None
    for field, value in vehiculoDependencia.model_dump(exclude_unset=True).items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete(db: Session, id: int):
    db_item = get_by_id(db, id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item