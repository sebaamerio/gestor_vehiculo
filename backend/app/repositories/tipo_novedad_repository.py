from sqlalchemy.orm import Session
from datetime import datetime
from ..models.tipo_novedad_model import TipoNovedad
from ..schemas.tipo_novedad_schema import TipoNovedadCreate


def get_all(db: Session):
    return (
        db.query(TipoNovedad)
        .filter(TipoNovedad.deleted_at.is_(None))
        .order_by(TipoNovedad.descripcion)
        .all()
    )


def get_by_id(db: Session, id: int):
    return (
        db.query(TipoNovedad)
        .filter(
            TipoNovedad.id == id,
            TipoNovedad.deleted_at.is_(None)
        )
        .first()
    )


def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return (
        db.query(TipoNovedad)
        .filter(
            TipoNovedad.descripcion.ilike(descripcion.strip()),
            TipoNovedad.deleted_at.is_(None)
        )
        .first()
    )


def create(db: Session, tipo_novedad: TipoNovedadCreate):
    db_tipo_novedad = TipoNovedad(
        descripcion=tipo_novedad.descripcion.strip()
    )
    db.add(db_tipo_novedad)
    db.commit()
    db.refresh(db_tipo_novedad)
    return db_tipo_novedad


def update(db: Session, id: int, tipo_novedad: TipoNovedadCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.descripcion = tipo_novedad.descripcion.strip()
    db.commit()
    db.refresh(db_tipo)
    return db_tipo


def delete(db: Session, id: int):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.deleted_at = datetime.utcnow()  # baja lógica
    db.commit()
    db.refresh(db_tipo)

    return db_tipo