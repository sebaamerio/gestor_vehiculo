from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import dependencia_repository
from ..schemas.dependencia_schema import DependenciaCreate


def get_all(db: Session): 
    return dependencia_repository.get_all(db)


def get_by_id(db: Session, id: int):
    tipo = dependencia_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de dependencia con id={id} no encontrado"
        )
    return tipo


def create(db: Session, dependencia: DependenciaCreate):
    existing = dependencia_repository.get_by_descripcion(db, dependencia.descripcion)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de dependencia '{dependencia.descripcion}' ya existe"
        )
    return dependencia_repository.create(db, dependencia)


def update(db: Session, id: int, dependencia: DependenciaCreate):   
    db_tipo = dependencia_repository.update(db, id, dependencia)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de dependencia con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = dependencia_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tipo de dependencia con id={id} no encontrado"
        )
    return {"message": f"Tipo de dependencia con id={id} eliminado correctamente"}