from sqlalchemy.orm import Session
from ..models.tipo_pago_model import TipoPago
from ..schemas.tipo_pago_schema import TipoPagoCreate

def get_all(db: Session):
    return db.query(TipoPago).order_by(TipoPago.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoPago).filter(TipoPago.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoPago).filter(
        TipoPago.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipo: TipoPagoCreate):
    db_tipo = TipoPago(
        descripcion=tipo.descripcion.strip()
    )
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def update(db: Session, id: int, tipo: TipoPagoCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.descripcion = tipo.descripcion.strip()
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