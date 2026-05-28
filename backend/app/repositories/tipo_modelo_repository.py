from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.tipo_modelo_model import TipoModelo
from ..schemas.tipo_modelo_schema import TipoModeloCreate

def get_all(db: Session):
    return db.query(TipoModelo).order_by(TipoModelo.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoModelo).filter(TipoModelo.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoModelo).filter(
        TipoModelo.descripcion.ilike(descripcion)
    ).first()


def create(db: Session, tipo_modelo: TipoModeloCreate):
    db_tipo_modelo = TipoModelo(**tipo_modelo.model_dump())
    db.add(db_tipo_modelo)
    db.commit()
    db.refresh(db_tipo_modelo)
    return db_tipo_modelo

def update(db: Session, id: int, tipo_modelo: TipoModeloCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None
    
    for field, value in tipo_modelo.model_dump(exclude_unset=True).items():
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