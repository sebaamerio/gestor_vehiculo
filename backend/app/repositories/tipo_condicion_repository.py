from sqlalchemy.orm import Session
from ..models.tipo_condicion_model import TipoCondicion
from ..schemas.tipo_condicion_schema import TipoCondicionCreate

def get_all(db: Session):
    return db.query(TipoCondicion).order_by(TipoCondicion.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoCondicion).filter(TipoCondicion.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoCondicion).filter(
        TipoCondicion.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipo_condicion: TipoCondicionCreate):
    db_tipo_condicion = TipoCondicion(**tipo_condicion.model_dump())
    db.add(db_tipo_condicion)
    db.commit()
    db.refresh(db_tipo_condicion)
    return db_tipo_condicion

def update(db: Session, id: int, tipo_condicion: TipoCondicionCreate): 
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    for field, value in tipo_condicion.model_dump(exclude_unset=True).items():
        setattr(db_tipo, field, value)

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