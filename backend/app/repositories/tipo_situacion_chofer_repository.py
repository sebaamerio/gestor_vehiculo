from sqlalchemy.orm import Session
from ..models.tipo_situacion_chofer_model import TipoSituacionChofer
from ..schemas.tipo_situacion_chofer_schema import TipoSituacionChoferCreate

def get_all(db: Session):
    return db.query(TipoSituacionChofer).order_by(TipoSituacionChofer.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoSituacionChofer).filter(TipoSituacionChofer.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoSituacionChofer).filter(
        TipoSituacionChofer.descripcion.ilike(descripcion)
    ).first()


def create(db: Session, tipo_situacion: TipoSituacionChoferCreate):
    db_tipo_situacion = TipoSituacionChofer(
        descripcion=tipo_situacion.descripcion.strip()
    )
    db.add(db_tipo_situacion)
    db.commit()
    db.refresh(db_tipo_situacion)
    return db_tipo_situacion

def update(db: Session, id: int, tipo_situacion: TipoSituacionChoferCreate):
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