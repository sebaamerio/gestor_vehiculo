from sqlalchemy.orm import Session
from ..models.tipo_vehiculo_model import TipoVehiculo
from ..schemas.tipo_vehiculo_schema import TipoVehiculoCreate

def get_all(db: Session):
    return db.query(TipoVehiculo).order_by(TipoVehiculo.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoVehiculo).filter(TipoVehiculo.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca un tipo de vehículo por su descripción (case insensitive)."""
    return db.query(TipoVehiculo).filter(
        TipoVehiculo.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipo_vehiculo: TipoVehiculoCreate):
    db_tipo_vehiculo = TipoVehiculo(
        descripcion=tipo_vehiculo.descripcion.strip()
    )
    db.add(db_tipo_vehiculo)
    db.commit()
    db.refresh(db_tipo_vehiculo)
    return db_tipo_vehiculo

def update(db: Session, id: int, tipo_vehiculo: TipoVehiculoCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.descripcion = tipo_vehiculo.descripcion.strip()
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def delete(db: Session, id: int):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db.delete(db_tipo)
    db.commit()
    return db_tipo