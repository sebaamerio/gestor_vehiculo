from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import chofer_repository
from ..schemas.chofer_schema import ChoferCreate, ChoferUpdate


def get_all(db: Session): 
    return chofer_repository.get_all(db)

def get_paginated(db, page, page_size, filter_field, filter_value, sort_field, sort_order):
    return chofer_repository.get_paginated(
        db=db,
        page=page,
        page_size=page_size,
        filter_field=filter_field,       
        filter_value=filter_value,
        sort_field=sort_field,
        sort_order=sort_order,
    )

def get_choferes_by_licencia(db: Session): 
    return chofer_repository.get_by_licencias(db)

def get_by_id(db: Session, id: int):
    tipo = chofer_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chofer con id={id} no encontrado"
        )
    return tipo


def create(db: Session, chofer: ChoferCreate):
    existing = chofer_repository.get_by_nombre(db, chofer.nombre)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Chofer '{chofer.descripcion}' ya existe"
        )
    return chofer_repository.create(db, chofer)


def update(db: Session, id: int, chofer: ChoferUpdate):   
    db_tipo = chofer_repository.update(db, id, chofer)
    if not db_tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chofer con id={id} no encontrado"
        )
    return db_tipo


def delete(db: Session, id: int):
    deleted = chofer_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chofer con id={id} no encontrado"
        )
    return {"message": f"Chofer con id={id} eliminado correctamente"}

