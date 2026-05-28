from sqlalchemy.orm import Session
from ..models.tipo_documento_model import TipoDocumento
from ..schemas.tipo_documento_schema import TipoDocumentoCreate

def get_all(db: Session):
    return db.query(TipoDocumento).order_by(TipoDocumento.descripcion).all()

def get_by_id(db: Session, id: int):
    return db.query(TipoDocumento).filter(TipoDocumento.id == id).first()

def get_by_descripcion(db: Session, descripcion: str):
    """Busca por su descripción (case insensitive)."""
    return db.query(TipoDocumento).filter(
        TipoDocumento.descripcion.ilike(descripcion)
    ).first()

def create(db: Session, tipo_documento: TipoDocumentoCreate):
    db_tipo_documento = TipoDocumento(
        descripcion=tipo_documento.descripcion.strip()
    )
    db.add(db_tipo_documento)
    db.commit()
    db.refresh(db_tipo_documento)
    return db_tipo_documento

def update(db: Session, id: int, tipo_documento: TipoDocumentoCreate):
    db_tipo = get_by_id(db, id)
    if not db_tipo:
        return None

    db_tipo.descripcion = tipo_documento.descripcion.strip()
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