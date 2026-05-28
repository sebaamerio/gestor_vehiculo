from sqlalchemy.orm import Session
from ..models.tipo_carroceria_model import TipoCarroceria
from ..schemas.tipo_carroceria_schema import TipoCarroceriaCreate

def get_all(db: Session):
    return db.query(TipoCarroceria).order_by(TipoCarroceria.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoCarroceria).filter(TipoCarroceria.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoCarroceria).filter(
        TipoCarroceria.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipo_arroceria: TipoCarroceriaCreate):
    db_tipo_arroceria = TipoCarroceria(
        descripcion=tipo_arroceria.descripcion.strip()
    )
    db.add(db_tipo_arroceria)
    db.commit()
    db.refresh(db_tipo_arroceria)
    return db_tipo_arroceria

def update(db: Session, id: int, tipo_arroceria: TipoCarroceriaCreate):   
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.descripcion = tipo_arroceria.descripcion.strip()
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