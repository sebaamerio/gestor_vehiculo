from sqlalchemy.orm import Session
from typing import Optional
from ..models.cambio_chasis_model import CambioChasis
from ..schemas.cambio_chasis_schema import CambioChasisUpdate
  
def get_all(db: Session):
  return db.query(CambioChasis).all()

def get_by_id(db: Session, id: int):
  return db.query(CambioChasis).filter(CambioChasis.id == id).first()

def get_by_novedad_id(db: Session, novedad_id: int) -> Optional[CambioChasis]:
    return db.query(CambioChasis).filter(CambioChasis.novedad_id == novedad_id).first()

def update(db: Session, id: int, data: CambioChasisUpdate):
    db_item = db.query(CambioChasis).filter(CambioChasis.id == id).first()
    if not db_item:
        return None

    # Actualizar solo el detalle
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)

    # Actualizar la Novedad asociada (solo fecha y observacion)
    if data.fecha or data.observaciones:
        db_novedad = db_item.novedad  # relación ORM
        if db_novedad:
            if data.fecha:
                db_novedad.fecha = data.fecha
            if data.observaciones:
                db_novedad.observaciones = data.observaciones

    # Actualizar Vehiculo usando la Novedad
    if data.chasis_nuevo:
        vehiculo = db_item.novedad.vehiculo   # <-- esto no requiere relación desde CambioChasis
        if vehiculo:
            vehiculo.chasis_nro = data.chasis_nuevo

    db.commit()
    db.refresh(db_item)
    return db_item  
