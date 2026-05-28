from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..repositories import transferencia_repository
from ..schemas.transferencia_schema import TransferenciaUpdate

def get_all(db: Session): 
    return transferencia_repository.get_all(db)

def get_by_id(db: Session, id: int):
    tipo = transferencia_repository.get_by_id(db, id)
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return tipo

def get_by_NovedadId(db: Session, novedad_id: int):
    item = transferencia_repository.get_by_novedad_id(db, novedad_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return item

def update(db: Session, id: int, data: TransferenciaUpdate):
    db_transferencia = transferencia_repository.update(db, id, data)
    if not db_transferencia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Novedad con id={id} no encontrado"
        )
    return db_transferencia
