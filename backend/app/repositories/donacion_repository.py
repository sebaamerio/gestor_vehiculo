from sqlalchemy.orm import Session
from typing import  Optional
from ..models.donacion_model import Donacion
from ..models.dependencia_model import Dependencia
from ..models.vehiculo_model import Vehiculo as VehiculoModel
from ..schemas.donacion_schema import DonacionUpdate
  
def get_all(db: Session):
  return db.query(Donacion).all()

def get_by_id(db: Session, id: int):
  return db.query(Donacion).filter(Donacion.id == id).first()

def get_by_novedad_id(db: Session, novedad_id: int) -> Optional[Donacion]:
    return db.query(Donacion).filter(Donacion.novedad_id == novedad_id).first()

def update(db: Session, id: int, data: DonacionUpdate):     
    db_donacion = db.query(Donacion).filter(Donacion.id == id).first()
    
    if db_donacion:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_donacion, key, value)
        
        db.commit()
        db.refresh(db_donacion)
        return db_donacion
        
    return None

def update(db: Session, id: int, data: DonacionUpdate):
    db_item = db.query(Donacion).filter(Donacion.id == id).first()
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

    dependencia = db.query(Dependencia).filter(Dependencia.id == data.dependencia_anterior_id).first()
    if dependencia:
        vehiculo = db.query(VehiculoModel).filter(VehiculoModel.id == db_novedad.vehiculo_id).first()
        if vehiculo:
            vehiculo.dependencia_id = dependencia.id

    db.commit()
    db.refresh(db_item)
    return db_item  
