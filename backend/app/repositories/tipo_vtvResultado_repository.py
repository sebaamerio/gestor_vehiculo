from sqlalchemy.orm import Session
from ..models.tipo_vtvResultado_model import TipoVtvResultado
from ..schemas.tipo_vtvResultado_schema import TipoVtvResultadoCreate

def get_all(db: Session):
    return db.query(TipoVtvResultado).order_by(TipoVtvResultado.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoVtvResultado).filter(TipoVtvResultado.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoVtvResultado).filter(
        TipoVtvResultado.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipo_resultadoVtv: TipoVtvResultadoCreate):
    db_tipo_resultadoVtv = TipoVtvResultado(
        descripcion=tipo_resultadoVtv.descripcion.strip()
    )
    db.add(db_tipo_resultadoVtv)
    db.commit()
    db.refresh(db_tipo_resultadoVtv)
    return db_tipo_resultadoVtv

def update(db: Session, id: int, tipo_resultadoVtv: TipoVtvResultadoCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.descripcion = tipo_resultadoVtv.descripcion.strip()
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