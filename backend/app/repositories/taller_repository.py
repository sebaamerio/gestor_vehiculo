from sqlalchemy.orm import Session
from ..models.taller_model import Taller
from ..schemas.taller_schema import TallerCreate, TallerUpdate

def get_all(db: Session):
    return db.query(Taller).order_by(Taller.taller_desc).all()

def get_by_id(db: Session, id: int):
    return db.query(Taller).filter(Taller.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(Taller).filter(
        Taller.taller_desc.ilike(descripcion)
    ).first()


def create(db: Session, data: TallerCreate):    
    taller = Taller(**data.model_dump())
    db.add(taller)
    db.commit()
    db.refresh(taller)
    return taller

def update(db: Session, id: int, data: TallerUpdate):
    taller = get_by_id(db, id)
    if not taller:
        return None

    for key, value in data.model_dump().items():
        setattr(taller, key, value)
    db.commit()
    db.refresh(taller)
    return taller

def delete(db: Session, id: int):
    taller = get_by_id(db, id)
    if not taller:
        return None

    db.delete(taller)
    db.commit()
    return taller