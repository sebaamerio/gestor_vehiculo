from sqlalchemy.orm import Session
from ..models.tipo_marca_model import TipoMarca
from ..schemas.tipo_marca_schema import TipoMarcaCreate

def get_all(db: Session):
    return db.query(TipoMarca).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoMarca).filter(TipoMarca.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca una TipoMarca por su descripción (case insensitive)."""
    return db.query(TipoMarca).filter(
        TipoMarca.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipoMarca: TipoMarcaCreate):
    nueva_tipoMarca = TipoMarca(**tipoMarca.model_dump())
    db.add(nueva_tipoMarca)
    db.commit()
    db.refresh(nueva_tipoMarca)
    return nueva_tipoMarca

def update(db: Session, id: int, tipoMarca: TipoMarcaCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.descripcion = tipoMarca.descripcion.strip()
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def delete(db: Session, id: int):
    db_tipoMarca = get_by_id(db, id)
    if db_tipoMarca:
        db.delete(db_tipoMarca)
        db.commit()
    return db_tipoMarca
