from sqlalchemy.orm import Session
from typing import Optional
from ..models.baja_model import Baja
from ..schemas.baja_schema import BajaUpdate

def get_all(db: Session):
    return db.query(Baja).all()

def get_by_id(db: Session, id: int):
    return db.query(Baja).filter(Baja.id == id).first()

def get_by_novedad_id(db: Session, novedad_id: int) -> Optional[Baja]:
    """Obtiene una baja asociada a una Novedad ID específica."""
    return db.query(Baja).filter(Baja.novedad_id == novedad_id).first()

def update(db: Session, id: int, baja: BajaUpdate):
    db_baja = db.query(Baja).filter(Baja.id == id).first()
    if not db_baja:
        return None

    update_data = baja.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_baja, key, value)

    db.commit()
    db.refresh(db_baja)
    return db_baja   
