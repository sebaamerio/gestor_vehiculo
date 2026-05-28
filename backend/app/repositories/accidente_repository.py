from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.accidente_model import Accidente
from ..schemas.accidente_schema import AccidenteUpdate

def get_all(db: Session):
  return db.query(Accidente).all()

def get_by_id(db: Session, id: int):
  return db.query(Accidente).filter(Accidente.id == id).first()

def get_by_novedad_id(db: Session, novedad_id: int) -> Optional[Accidente]:
    """Obtiene una accidente asociada a una Novedad ID específica."""
    return db.query(Accidente).filter(Accidente.novedad_id == novedad_id).first()

def update(db: Session, id: int, data: AccidenteUpdate):
    db_item = db.query(Accidente).filter(Accidente.id == id).first()
    if not db_item:
        return None

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item