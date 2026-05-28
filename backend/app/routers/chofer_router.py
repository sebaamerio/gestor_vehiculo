from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.chofer_schema import (
    Chofer,
    ChoferCreate,
    ChoferUpdate,
    ChoferPaginated,
    ChoferesByLicencia)
from ..services import chofer_service

router = APIRouter(prefix="/chofer", tags=["Chofer"], dependencies=[Depends(get_current_user)])


@router.get("/report/byLicencia", response_model=list[ChoferesByLicencia])
def get_by_licencia(db: Session = Depends(get_db)):
    return chofer_service.get_choferes_by_licencia(db)

@router.get("/", response_model=ChoferPaginated)
def list( page: int = 0,
    page_size: int = 15,
    filter_field: str | None = None,
    filter_value: str | None = None,
    sort_field: str | None = None,
    sort_order: str | None = None,  # "asc" o "desc",
    db: Session = Depends(get_db)):
    return chofer_service.get_paginated(
        db=db,
        page=page,
        page_size=page_size,
        filter_field=filter_field,
        filter_value=filter_value,
        sort_field=sort_field,
        sort_order=sort_order,
    )

@router.get("/{id}", response_model=Chofer)
def get(id: int, db: Session = Depends(get_db)):
    return chofer_service.get_by_id(db, id)


@router.post("/", response_model=Chofer, dependencies=[Depends(require_role("admin"))])
def create(data: ChoferCreate, db: Session = Depends(get_db)):
    return chofer_service.create(db, data)


@router.put("/{id}", response_model=Chofer, dependencies=[Depends(require_role("admin"))])
def update(id: int, data: ChoferUpdate, db: Session = Depends(get_db)):
    return chofer_service.update(db, id, data)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete(id: int, db: Session = Depends(get_db)):
    return chofer_service.delete(db, id)