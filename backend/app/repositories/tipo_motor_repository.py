from sqlalchemy.orm import Session
from ..models.tipo_motor_model import TipoMotor
from ..schemas.tipo_motor_schema import TipoMotorCreate

def get_all(db: Session):
    return db.query(TipoMotor).order_by(TipoMotor.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoMotor).filter(TipoMotor.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoMotor).filter(
        TipoMotor.descripcion.ilike(descripcion)
    ).first()


def create(db: Session, tipo_motor: TipoMotorCreate):
    db_tipo_motor = TipoMotor(
        descripcion=tipo_motor.descripcion.strip()
    )
    db.add(db_tipo_motor)
    db.commit()
    db.refresh(db_tipo_motor)
    return db_tipo_motor

def update(db: Session, id: int, tipo_motor: TipoMotorCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.descripcion = tipo_motor.descripcion.strip()
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