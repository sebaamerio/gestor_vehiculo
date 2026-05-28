from sqlalchemy.orm import Session
from ..models.tipo_traccion_model import TipoTraccion
from ..schemas.tipo_traccion_schema import TipoTraccionCreate

def get_all(db: Session):
    return db.query(TipoTraccion).order_by(TipoTraccion.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoTraccion).filter(TipoTraccion.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoTraccion).filter(
        TipoTraccion.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipo: TipoTraccionCreate):
    db_tipo = TipoTraccion(
        descripcion=tipo.descripcion.strip()
    )
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def update(db: Session, id: int, tipo: TipoTraccionCreate):
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