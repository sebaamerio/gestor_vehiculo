from sqlalchemy.orm import Session
from typing import Optional
from ..models.transferencia_model import Transferencia
from ..models.dependencia_model import Dependencia
from ..models.vehiculo_model import Vehiculo as VehiculoModel
from ..models.vehiculo_dependencia_model import VehiculoDependencia

from ..schemas.transferencia_schema import TransferenciaUpdate

def get_all(db: Session):
  return db.query(Transferencia).all()

def get_by_id(db: Session, id: int):
  return db.query(Transferencia).filter(Transferencia.id == id).first()

def get_by_novedad_id(db: Session, novedad_id: int) -> Optional[Transferencia]:   
    return db.query(Transferencia).filter(Transferencia.novedad_id == novedad_id).first()

def update(db: Session, id: int, item: TransferenciaUpdate):
    db_transf = db.query(Transferencia).filter(Transferencia.id == id).first()
    
    if not db_transf:
        return None

    # =====================================
    # 1. ACTUALIZAR DETALLE
    # =====================================
    update_data = item.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_transf, key, value)

    # =====================================
    # 2. ACTUALIZAR NOVEDAD
    # =====================================
    db_novedad = db_transf.novedad

    if db_novedad:
        if item.fecha:
            db_novedad.fecha = item.fecha
        if item.observaciones:
            db_novedad.observaciones = item.observaciones

    # =====================================
    # 3. ACTUALIZAR DEPENDENCIA ACTIVA
    # POR AHORA QUEDA
    # =====================================
    #if item.dependencia_id:
    #    dependencia = db.query(Dependencia).filter(
    #        Dependencia.id == item.dependencia_id
    #    ).first()
    #
    #    if not dependencia:
    #        raise ValueError("Dependencia no encontrada")
    #
    #    # 🔥 buscar dependencia activa del vehículo
    #    dependencia_activa = db.query(VehiculoDependencia).filter(
    #        VehiculoDependencia.vehiculo_id == db_novedad.vehiculo_id,
    #        VehiculoDependencia.activo == True
    #    ).first()
    #
    #    if not dependencia_activa:
    #        raise ValueError("No existe dependencia activa")
    #
    #    # ✅ SOLO si cambió
    #    if dependencia_activa.dependencia_id != item.dependencia_id:
    #        dependencia_activa.dependencia_id = item.dependencia_id
    #        dependencia_activa.dependencia_descripcion = dependencia.descripcion

    # =====================================
    # 4. GUARDAR
    # =====================================
    db.commit()
    db.refresh(db_transf)

    return db_transf