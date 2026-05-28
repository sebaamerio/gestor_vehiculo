from sqlalchemy.orm import Session
from ..models.tipo_situacion_model import TipoSituacion
from ..schemas.tipo_situacion_schema import TipoSituacionCreate

def get_all(db: Session):
    return db.query(TipoSituacion).order_by(TipoSituacion.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoSituacion).filter(TipoSituacion.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoSituacion).filter(
        TipoSituacion.descripcion.ilike(descripcion)
    ).first()


def create(db: Session, tipo_situacion: TipoSituacionCreate):
    db_tipo_situacion = TipoSituacion(
        descripcion=tipo_situacion.descripcion.strip()
    )
    db.add(db_tipo_situacion)
    db.commit()
    db.refresh(db_tipo_situacion)
    return db_tipo_situacion

def update(db: Session, id: int, tipo_situacion: TipoSituacionCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.descripcion = tipo_situacion.descripcion.strip()
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