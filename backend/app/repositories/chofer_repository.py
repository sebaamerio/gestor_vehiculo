from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, or_, func, case
from datetime import date
from ..models.chofer_model import Chofer
from ..schemas.chofer_schema import ChoferCreate, ChoferUpdate

def get_all(db: Session):
    return db.query(Chofer).all()
from sqlalchemy import asc, desc, or_
from sqlalchemy.orm import Session

def get_paginated(
    db: Session,
    page: int,
    page_size: int,
    filter_field: str | None = None,
    filter_value: str | None = None,
    sort_field: str | None = None,
    sort_order: str | None = None,
):
    query = db.query(Chofer)

    # 🔎 FILTRO: aplica siempre ANTES de contar
    if filter_field and filter_value:
        column = getattr(Chofer, filter_field, None)
        if column is not None:
            query = query.filter(column.ilike(f"{filter_value}%"))

    # 🔢 Total filtrado (MUI lo necesita)
    total = query.count()

    # ↕️ ORDENAMIENTO
    if sort_field:
        column = getattr(Chofer, sort_field, None)
        if column is not None:
            query = query.order_by(
                asc(column) if sort_order == "asc" else desc(column)
            )

    # 📄 PAGINACIÓN
    results = (
        query
        .offset(page * page_size)
        .limit(page_size)
        .all()
    )
    return {"total": total, "data": results}


def get_by_id(db: Session, chofer_id: int):
    return db.query(Chofer).filter(Chofer.id == chofer_id).first()

def get_by_nombre(db: Session, nombre: str):   
    return db.query(Chofer).filter(
        Chofer.nombre.ilike(nombre)
    ).first()

def create(db: Session, data: ChoferCreate):
    chofer = Chofer(**data.model_dump())
    db.add(chofer)
    db.commit()
    db.refresh(chofer)
    return chofer

def update(db: Session, chofer_id: int, data: ChoferUpdate):
    chofer = get_by_id(db, chofer_id)
    if not chofer:
        return None
    for key, value in data.model_dump().items():
        setattr(chofer, key, value)
    db.commit()
    db.refresh(chofer)
    return chofer

def delete(db: Session, chofer_id: int):
    chofer = get_by_id(db, chofer_id)
    if not chofer:
        return None
    db.delete(chofer)
    db.commit()
    return chofer

###############
# Reportes
###############
def get_by_licencias(db: Session):
    today = date.today()

    estado = case(
        (Chofer.licencia_vto == None, "Sin fecha"),
        (Chofer.licencia_vto < today, "Vencidas"),
        else_="Vigentes"
    )

    results = db.query(
        estado.label("descripcion"),
        func.count(Chofer.id).label("value")
    ).group_by(estado).all()

    return [{"descripcion": r.descripcion, "value": r.value} for r in results]