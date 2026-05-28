from sqlalchemy.orm import Session
from typing import Optional
from ..models.robo_model import Robo
from ..models.tipo_situacion_model import TipoSituacion
from ..schemas.robo_schema import RoboUpdate
  
def get_all(db: Session):
  return db.query(Robo).all()

def get_by_id(db: Session, id: int):
  return db.query(Robo).filter(Robo.id == id).first()

def get_by_novedad_id(db: Session, novedad_id: int) -> Optional[Robo]:
    return db.query(Robo).filter(Robo.novedad_id == novedad_id).first()

def update(db: Session, id: int, item: RoboUpdate):
    db_robo = db.query(Robo).filter(Robo.id == id).first()
    if not db_robo:
        return None

    # =====================================
    # 1) Actualizar detalle
    # =====================================
    update_data = item.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_robo, key, value)

    # =====================================
    # 2) Actualizar Novedad
    # =====================================
    if item.fecha or item.observaciones:
        db_novedad = db_robo.novedad  # relación ORM
        if db_novedad:
            if item.fecha:
                db_novedad.fecha = item.fecha
            if item.observaciones:
                db_novedad.observaciones = item.observaciones

    # =====================================
    # 🔥 3) SI HAY FECHA_RECUPERO → VEHÍCULO ACTIVO
    # =====================================
    db_novedad = db_robo.novedad

    if db_novedad and db_novedad.vehiculo:
        descripcion = "ACTIVO" if item.fecha_recupero else "BAJA"

        tipo = db.query(TipoSituacion).filter(
            TipoSituacion.descripcion == descripcion
        ).first()

        if tipo:
            db_novedad.vehiculo.tipo_situacion = tipo

    # =====================================
    # 4) Guardar
    # =====================================
    db.commit()
    db.refresh(db_robo)
    return db_robo   
