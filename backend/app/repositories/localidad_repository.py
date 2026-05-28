from sqlalchemy.orm import Session
from ..models.localidad_model import Localidad
from ..schemas.localidad_schema import LocalidadCreate, LocalidadUpdate

def get_all(db: Session):   
  return db.query(Localidad).order_by(Localidad.descripcion.asc()).all()

def get_by_id(db: Session, id: int):
    return db.query(Localidad).filter(Localidad.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(Localidad).filter(
        Localidad.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, localidad: LocalidadCreate):
    db_localidad = Localidad(**localidad.model_dump())
    db.add(db_localidad)
    db.commit()
    db.refresh(db_localidad)
    return db_localidad

def update(db: Session, id: int, localidad: LocalidadUpdate):
    db_localidad = get_by_id(db, id)
    if not db_localidad:
        return None
    
    # ✅ Solo actualiza los campos enviados
    for field, value in localidad.model_dump(exclude_unset=True).items():
        setattr(db_localidad, field, value)

    db.commit()
    db.refresh(db_localidad)
    return db_localidad

def delete(db: Session, id: int):
    db_localidad = get_by_id(db, id)
    if db_localidad:
        db.delete(db_localidad)
        db.commit()
    return db_localidad
