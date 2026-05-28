from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_situacion_schema import TipoSituacion, TipoSituacionCreate
from ..services import tipo_situacion_service

router = APIRouter(prefix="/tipo_situacion", tags=["TipoSituacion"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoSituacion])
def list_tipo_situacion(db: Session = Depends(get_db)):
    return tipo_situacion_service.get_all(db)


@router.get("/{id}", response_model=TipoSituacion)
def get_tipo_situacion(id: int, db: Session = Depends(get_db)):
    return tipo_situacion_service.get_by_id(db, id)


@router.post("/", response_model=TipoSituacion, dependencies=[Depends(require_role("admin"))])
def create_tipo_situacion(tipo_vehiculo: TipoSituacionCreate, db: Session = Depends(get_db)):
    return tipo_situacion_service.create(db, tipo_vehiculo)


@router.put("/{id}", response_model=TipoSituacion, dependencies=[Depends(require_role("admin"))])
def update_tipo_situacion(id: int, tipo_vehiculo: TipoSituacionCreate, db: Session = Depends(get_db)):
    return tipo_situacion_service.update(db, id, tipo_vehiculo)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_situacion(id: int, db: Session = Depends(get_db)):
    return tipo_situacion_service.delete(db, id)
