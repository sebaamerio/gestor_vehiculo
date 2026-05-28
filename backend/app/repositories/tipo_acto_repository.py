from sqlalchemy.orm import Session
from ..models.tipo_acto_model import TipoActo
from ..schemas.tipo_acto_schema import TipoActoCreate

def get_all(db: Session):
    return db.query(TipoActo).order_by(TipoActo.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoActo).filter(TipoActo.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoActo).filter(
        TipoActo.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipo_acto: TipoActoCreate):
    db_tipo_acto = TipoActo(
        descripcion=tipo_acto.descripcion.strip()
    )
    db.add(db_tipo_acto)
    db.commit()
    db.refresh(db_tipo_acto)
    return db_tipo_acto

def update(db: Session, id: int, tipo_acto: TipoActoCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.descripcion = tipo_acto.descripcion.strip()
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