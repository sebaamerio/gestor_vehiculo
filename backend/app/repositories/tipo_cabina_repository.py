from sqlalchemy.orm import Session
from ..models.tipo_cabina_model import TipoCabina
from ..schemas.tipo_cabina_schema import TipoCabinaCreate

def get_all(db: Session):
    return db.query(TipoCabina).order_by(TipoCabina.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoCabina).filter(TipoCabina.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoCabina).filter(
        TipoCabina.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipo: TipoCabinaCreate):
    db_tipo = TipoCabina(
        descripcion=tipo.descripcion.strip()
    )
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def update(db: Session, id: int, tipo: TipoCabinaCreate):
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