from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import tipo_documento_repository
from ..schemas.tipo_documento_schema import TipoDocumentoCreate


def get_all(db: Session): 
    return tipo_documento_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = tipo_documento_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de documento con id={id} no encontrado"
        )
    return tipo


def create(db: Session, tipo_documento: TipoDocumentoCreate):
    existing = tipo_documento_repository.get_by_descripcion(db, tipo_documento.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de documento '{tipo_documento.descripcion}' ya existe"
        )
    return tipo_documento_repository.create(db, tipo_documento)


def update(db: Session, id: int, tipo_documento: TipoDocumentoCreate):   
    db_tipo = tipo_documento_repository.update(db, id, tipo_documento)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de documento con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = tipo_documento_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de documento con id={id} no encontrado"
        )
    return {"message": f"Tipo de documento con id={id} eliminado correctamente"}
