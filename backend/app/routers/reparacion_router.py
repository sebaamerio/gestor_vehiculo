from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.reparacion_schema import Reparacion, ReparacionCreate, ReparacionUpdate
from ..services import reparacion_service

router = APIRouter(prefix="/reparacion", tags=["Reparacion"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=list[Reparacion])
def list_reparaciones(db: Session = Depends(get_db)):
    return reparacion_service.get_all(db)


@router.get("/{id}", response_model=Reparacion)
def get_reparacion(id: int, db: Session = Depends(get_db)):
    return reparacion_service.get_by_id(db, id)


@router.post("/", response_model=Reparacion, dependencies=[Depends(require_role("admin"))])
def create_reparacion(data: ReparacionCreate, db: Session = Depends(get_db)):
    return reparacion_service.create(db, data)


@router.put("/{id}", response_model=Reparacion, dependencies=[Depends(require_role("admin"))])
def update_reparacion(id: int, data: ReparacionUpdate, db: Session = Depends(get_db)):
    return reparacion_service.update(db, id, data)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_reparacion(id: int, db: Session = Depends(get_db)):
    return reparacion_service.delete(db, id)