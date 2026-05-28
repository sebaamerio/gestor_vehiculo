from sqlalchemy.orm import Session
from typing import Optional
from ..models.infraccion_model import Infraccion
from ..schemas.infraccion_schema import InfraccionUpdate

def get_all(db: Session):
  return db.query(Infraccion).all()

def get_by_id(db: Session, id: int):
  return db.query(Infraccion).filter(Infraccion.id == id).first()

def get_by_novedad_id(db: Session, novedad_id: int) -> Optional[Infraccion]:
    """Obtiene una infraccion asociada a una Novedad ID específica."""
    return db.query(Infraccion).filter(Infraccion.novedad_id == novedad_id).first()

def update(db: Session, id: int, data: InfraccionUpdate):
    db_item = db.query(Infraccion).filter(Infraccion.id == id).first()
    if not db_item:
        return None

    # Actualizar solo el detalle
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)

    # 🔥 Actualizar la Novedad asociada (solo fecha y observacion)
    if data.fecha or data.observaciones:
        db_novedad = db_item.novedad  # relación ORM
        if db_novedad:
            if data.fecha:
                db_novedad.fecha = data.fecha
            if data.observaciones:
                db_novedad.observaciones = data.observaciones

    db.commit()
    db.refresh(db_item)
    return db_item