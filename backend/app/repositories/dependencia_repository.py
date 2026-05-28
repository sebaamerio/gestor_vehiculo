from sqlalchemy.orm import Session
from ..models.dependencia_model import Dependencia
from ..schemas.dependencia_schema import DependenciaCreate

def get_all(db: Session):
    return db.query(Dependencia).order_by(Dependencia.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(Dependencia).filter(Dependencia.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(Dependencia).filter(
        Dependencia.descripcion.ilike(descripcion)
    ).first()


def create(db: Session, dependencia: DependenciaCreate):
    db_dependencia = Dependencia(**dependencia.model_dump())
    db.add(db_dependencia)
    db.commit()
    db.refresh(db_dependencia)
    return db_dependencia

def update(db: Session, id: int, dependencia: DependenciaCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    for field, value in dependencia.model_dump(exclude_unset=True).items():
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