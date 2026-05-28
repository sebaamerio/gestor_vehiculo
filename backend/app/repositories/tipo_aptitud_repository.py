from sqlalchemy.orm import Session
from ..models.tipo_aptitud_model import TipoAptitud
from ..schemas.tipo_aptitud_schema import TipoAptitudCreate

def get_all(db: Session):
    return db.query(TipoAptitud).order_by(TipoAptitud.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoAptitud).filter(TipoAptitud.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoAptitud).filter(
        TipoAptitud.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipo: TipoAptitudCreate):
    db_tipo = TipoAptitud(
        descripcion=tipo.descripcion.strip()
    )
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def update(db: Session, id: int, tipo: TipoAptitudCreate):
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